# PolyFiller
 
PolyFiller is a tool written in Python to generate location based points within a certain geographical area. <br> 
By reading through a provided .KML file it generates points within that area.

# Dependencies

PolyFiller uses the following libraries and it's dependencies:

- fastkml
- Geometry
- PySimpleGUI
- Shapely
- mapbox

# KML Requirements

To generate the best possible CSV file the following things have to be in order:

<br>

> The name header and filename:

```html
<name>FR_Toulouse</name>       <!--country_prefix + city_name-->
```

> The polygon attributes:
```html
<name>55</name>                                         <!--zone_code-->
<description><![CDATA[<p>4 - 4,99</p>]]></description>  <!--tariff_range-->
<styleUrl>#style4</styleUrl>                       <!--correct styleUrl-->
```

> The coordinates:
```html
<coordinates>
    1.4296621437324202,43.59769370449716,0.000
    1.4297810655126266,43.59739690720332,0.000
    1.4233531058265607,43.59631504510464,0.000      <!--A well formed polygon-->
    1.4232247343,43.5966013783,0.000
    1.4296621437324202,43.59769370449716,0.000
</coordinates>
```
<br>

### Output CSV


| ZONE_CODE | LAT         | LON         | CITY     | DISPLAY_STREETNAME       | GOOGLE_STREETNAME        | ZONE_STREET              | ZONE_DESCRIPTION   | Tariff_range | Unieke ID |
|-----------|-------------|-------------|----------|--------------------------|--------------------------|--------------------------|--------------------|--------------|-----------|
| 55        | 43,59721367 | 1,428610331 | Toulouse | Avenue Étienne Billières | Avenue Étienne Billières | Avenue Étienne Billières | Toulouse - Zone 55 | 3 - 3,99     | FRTOU35   |
