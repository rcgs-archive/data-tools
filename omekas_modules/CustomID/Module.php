<?php
namespace CustomID;

use Omeka\Api\Adapter\ItemAdapter;
use Omeka\Module\AbstractModule;
use Laminas\EventManager\Event;
use Laminas\EventManager\SharedEventManagerInterface;

class Module extends AbstractModule
{
    /** @var int gc:resourceIdentifier の property_id */
    const RECORD_ID_PROPERTY_ID = 2176;

    const RECORD_ID_TERM = 'gc:resourceIdentifier';

    /** @var int 連番の桁数（例: PACKAGE0000001） */
    const SERIAL_LENGTH = 7;

    /**
     * リソーステンプレート ID => resourceIdentifier プレフィックス
     *
     * @var array<int, string>
     */
    const TEMPLATE_PREFIXES = [
        13 => 'AGENT',
        15 => 'CONTENTRATING',
        16 => 'RATINGDESCRIPTOR',
        22 => 'TOPIC',
        11 => 'VARIATION',
        9 => 'PLATFORM',
        10 => 'MEDIAFORMAT',
        12 => 'WORK',
        19 => 'ITEM',
        18 => 'DEVICE',
        17 => 'CONTRIBUTOR',
        21 => 'RELATEDINSTANCE',
        20 => 'PACKAGE',
    ];

    public function attachListeners(SharedEventManagerInterface $sharedEventManager)
    {
        $sharedEventManager->attach(
            ItemAdapter::class,
            'api.create.pre',
            [$this, 'generateNextRecordId']
        );
    }

    public function generateNextRecordId(Event $event)
    {
        /** @var \Omeka\Api\Request $request */
        $request = $event->getParam('request');
        $resource = $request->getContent();

        $templateId = $this->getResourceTemplateId($resource['o:resource_template'] ?? null);
        if ($templateId === null || !isset(self::TEMPLATE_PREFIXES[$templateId])) {
            return;
        }

        if ($this->hasRecordId($resource)) {
            return;
        }

        $prefix = self::TEMPLATE_PREFIXES[$templateId];
        $newId = $prefix . $this->getNextSerial($prefix);

        $resource[self::RECORD_ID_TERM][] = [
            'type' => 'literal',
            'property_id' => self::RECORD_ID_PROPERTY_ID,
            'is_public' => true,
            '@value' => $newId,
        ];

        $request->setContent($resource);
    }

    protected function getNextSerial(string $prefix): string
    {
        $connection = $this->getServiceLocator()->get('Omeka\Connection');
        $sql = 'SELECT MAX(`value`) FROM `value` WHERE property_id = :property_id AND `value` LIKE :prefix';
        $currentMax = $connection->fetchOne($sql, [
            'property_id' => self::RECORD_ID_PROPERTY_ID,
            'prefix' => $prefix . '%',
        ]);

        if ($currentMax) {
            $currentNumber = (int) substr($currentMax, strlen($prefix));
            $nextNumber = $currentNumber + 1;
        } else {
            $nextNumber = 1;
        }

        return str_pad((string) $nextNumber, self::SERIAL_LENGTH, '0', STR_PAD_LEFT);
    }

    /**
     * @param mixed $template
     */
    protected function getResourceTemplateId($template): ?int
    {
        if (is_numeric($template)) {
            return (int) $template;
        }
        if (is_object($template) && method_exists($template, 'id')) {
            return (int) $template->id();
        }
        if (is_array($template)) {
            if (isset($template['o:id'])) {
                return (int) $template['o:id'];
            }
            if (isset($template['value_resource_id'])) {
                return (int) $template['value_resource_id'];
            }
        }
        return null;
    }

    protected function hasRecordId(array $resource): bool
    {
        if (empty($resource[self::RECORD_ID_TERM]) || !is_array($resource[self::RECORD_ID_TERM])) {
            return false;
        }
        foreach ($resource[self::RECORD_ID_TERM] as $value) {
            if (!is_array($value)) {
                continue;
            }
            $text = $value['@value'] ?? $value['value'] ?? null;
            if ($text !== null && $text !== '') {
                return true;
            }
        }
        return false;
    }
}
