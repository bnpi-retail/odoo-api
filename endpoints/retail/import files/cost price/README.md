## Эндпоинт: /api/v1/retail/import/cost_price

### Описание:
Эндпоинт предназначен для иморта себестоимости товаров

### Метод запроса:
POST

### Принимаемые параметры:

1. **file (в формате XML):**
   - Описание: Файл данных в формате XML, который содержит данные по товарам.

2. **data_for_download:**
   - Описание: Параметр, который определяет тип данных для загрузки.
   - Возможные значения:
     - `cost_price`: Загрузить данные о себестоимости товаров.

### Структура XML-файла:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<offers>
	<offer>
		<id>b668b3fe-fde3-11e8-80ba-005056b96f56</id>
		<artikul>063259</artikul>
		<name>Дисплей для Samsung Galaxy J4 2018 SM-J400F золотой</name>
		<priceOzoneBase>5235</priceOzoneBase>
		<priceOzoneOld>9341</priceOzoneOld>
		<CostPrice>3764</CostPrice>
		<picture>https://www.mobparts.ru/upload/iblock/6ed/99c45p18ouejtp123i87dzcztewvfuqa.jpg</picture>
		<height>0.5</height>
		<width>0.7</width>
		<depth>0.7</depth>
		<weight>0.1</weight>
		<description>GH97-21915B</description>
		<VidTovara>Дисплеи для смартфонов</VidTovara>
		<ozon_category_id/>
		<ozon_title/>
		<ozon_fulltitle/>
	</offer>
	<!-- Другие предложения могут следовать здесь -->
</offers>