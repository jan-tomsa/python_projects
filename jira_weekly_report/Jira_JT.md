

```python
import pandas as pd
import numpy as np
import re
import requests
import urllib.request
import json

from time import sleep
from datetime import datetime
from jira import JIRA
from pandas.io.json import json_normalize
```


```python
jira = JIRA('https://czjira.ness.com', basic_auth=('jméno', 'heslo"'))
```


```python
issues = jira.search_issues('filter=33140', maxResults=500)
# Definování a naplnění polí
key = ([issue.key for issue in issues])
summary = ([issue.fields.summary for issue in issues])
issuetype = ([issue.fields.issuetype for issue in issues])
priority = ([issue.fields.priority for issue in issues])
status = ([issue.fields.status for issue in issues])
updated = ([issue.fields.updated for issue in issues])
reporter = ([issue.fields.reporter.displayName for issue in issues])
due = ([issue.fields.duedate for issue in issues])
labels = ([issue.fields.labels for issue in issues])
fixversion = ([issue.fields.fixVersions for issue in issues])
```


```python
#definování názvů sloupců 
tickety = {'type': issuetype,
            'key': key,
            'summary': summary,
            'priority': priority,
            'status': status,
            'updated': updated,
            'due': due,
            'labels': labels,
            'fixversion': fixversion}
```


```python
# pandas
DF = pd.DataFrame.from_dict(tickety)
```


```python
#srovná sloupce do pořadí 
JT = DF[["type","key","summary","priority","status","updated","due","labels","fixversion"]]
```


```python
#vybere vše ve sloupci summary, kde je obsažené slovo clone
#clone = JT[JT['summary'].str.contains('CLONE')]
```


```python
#vybere vše mimo ...
JT2 = JT[~JT['summary'].str.contains('CLONE')]
JT3 = JT2[~JT2['key'].str.contains('RUIANADM-19')]
JT4 = JT3[~JT3['key'].str.contains('RUIANADM-1086')]
#JT5 = JT4[JT4['labels'].loc.contains('Long_task')] - tady mám problém, budu muset vymazat [] ještě před pandasem :) 
```


```python
#seřazení 
JT4.sort_values(by = ['updated'], ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>key</th>
      <th>summary</th>
      <th>priority</th>
      <th>status</th>
      <th>updated</th>
      <th>due</th>
      <th>labels</th>
      <th>fixversion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>114</th>
      <td>Task</td>
      <td>CUZKRUIAN-18503</td>
      <td>TEST - Interpretovat výsledky BT RÚIAN 2.4</td>
      <td>Major</td>
      <td>Open</td>
      <td>2018-03-29T14:31:43.000+0200</td>
      <td>2018-03-29</td>
      <td>[]</td>
      <td>[xRUIAN-2.4 (plán)]</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Task</td>
      <td>CUZKRUIAN-18518</td>
      <td>Režie Jan Tomsa</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2018-03-29T10:51:46.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Chyba z testování</td>
      <td>CUZKRUIAN-18505</td>
      <td>PROD - migrace RUIAN-2.4 - služba RuianCtiSezn...</td>
      <td>Critical</td>
      <td>Open</td>
      <td>2018-03-27T13:44:09.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-2.4 (plán)]</td>
    </tr>
    <tr>
      <th>142</th>
      <td>Sub-task</td>
      <td>CUZKRUIAN-17543</td>
      <td>Prezentační servery - NZ</td>
      <td>Critical</td>
      <td>Reopened</td>
      <td>2018-03-23T19:41:45.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-2.5 (Plán)]</td>
    </tr>
    <tr>
      <th>143</th>
      <td>Nová modifikace</td>
      <td>CUZKRUIAN-17542</td>
      <td>Prezentační servery - NZ - Apache 2.4</td>
      <td>Major</td>
      <td>Open</td>
      <td>2018-03-23T19:41:34.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-2.5 (Plán)]</td>
    </tr>
    <tr>
      <th>156</th>
      <td>Sub-task</td>
      <td>CUZKRUIAN-17332</td>
      <td>Migrace z mod_wl na standardní moduly Apache</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2018-03-23T19:41:03.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-2.5 (Plán)]</td>
    </tr>
    <tr>
      <th>124</th>
      <td>Improvement</td>
      <td>CUZKRUIAN-18045</td>
      <td>DOCS - Aktualizace systémové příručky</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2018-03-23T19:35:26.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-2.4 (plán)]</td>
    </tr>
    <tr>
      <th>125</th>
      <td>Improvement</td>
      <td>CUZKRUIAN-18044</td>
      <td>EA - Aktualizace EA</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2018-03-23T19:35:21.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-2.4 (plán)]</td>
    </tr>
    <tr>
      <th>126</th>
      <td>Improvement</td>
      <td>CUZKRUIAN-18043</td>
      <td>DOCS - Aktualizace provozní dokumentace</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2018-03-23T19:35:02.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-2.4 (plán)]</td>
    </tr>
    <tr>
      <th>167</th>
      <td>Nová modifikace</td>
      <td>CUZKRUIAN-17097</td>
      <td>ISÚI: Omezení logů pro dotazy do historie (sys...</td>
      <td>Major</td>
      <td>Open</td>
      <td>2018-03-23T17:31:06.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>153</th>
      <td>Nová modifikace</td>
      <td>CUZKRUIAN-17418</td>
      <td>Úprava spouštění Microstation</td>
      <td>Major</td>
      <td>Open</td>
      <td>2018-03-21T13:48:02.000+0100</td>
      <td>None</td>
      <td>[Požadováno_do_R2.3]</td>
      <td>[xRUIAN-2.5 (Plán)]</td>
    </tr>
    <tr>
      <th>163</th>
      <td>Chyba z testování</td>
      <td>CUZKRUIAN-17215</td>
      <td>Instalační příručka – doplnění instrukcí k vyp...</td>
      <td>Major</td>
      <td>Open</td>
      <td>2018-03-21T13:44:14.000+0100</td>
      <td>None</td>
      <td>[@TODO]</td>
      <td>[xRUIAN-2.5 (Plán)]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bug</td>
      <td>RUIANADM-1337</td>
      <td>Pomalý první přístup na SharePoint: https://cz...</td>
      <td>Minor</td>
      <td>In Progress</td>
      <td>2018-03-19T12:01:12.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>176</th>
      <td>Nová modifikace</td>
      <td>CUZKRUIAN-16803</td>
      <td>XSD pro EWS (A3S) na adrese https://isui.cuzk....</td>
      <td>Major</td>
      <td>Open</td>
      <td>2018-03-16T09:37:59.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-2.5 (Plán)]</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Chyba z testování</td>
      <td>CUZKRUIAN-18445</td>
      <td>Prvek je zamčen.</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2018-03-15T16:32:15.000+0100</td>
      <td>2018-03-07</td>
      <td>[]</td>
      <td>[xRUIAN-2.4 (plán)]</td>
    </tr>
    <tr>
      <th>129</th>
      <td>Chyba z testování</td>
      <td>CUZKRUIAN-17943</td>
      <td>CR041 – Zobrazení chybové hlášky SO0401 v příp...</td>
      <td>Major</td>
      <td>Need More Information</td>
      <td>2018-03-15T15:18:55.000+0100</td>
      <td>None</td>
      <td>[Nezbytné_vR2.3]</td>
      <td>[xRUIAN-2.4 (plán)]</td>
    </tr>
    <tr>
      <th>162</th>
      <td>Provozní údržba na objednávku</td>
      <td>CUZKRUIAN-17217</td>
      <td>UNIX: Rozšíření předání instalačních dávek RÚI...</td>
      <td>Major</td>
      <td>Open</td>
      <td>2018-03-15T14:20:04.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Sub-task</td>
      <td>RUIANADM-1339</td>
      <td>Support report 2018-02</td>
      <td>Major</td>
      <td>In Progress</td>
      <td>2018-03-14T09:19:38.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Sub-task</td>
      <td>RUIANADM-1310</td>
      <td>Support report 2018-01</td>
      <td>Major</td>
      <td>In Progress</td>
      <td>2018-03-14T09:17:53.000+0100</td>
      <td>2017-07-18</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sub-task</td>
      <td>RUIANADM-1323</td>
      <td>RUIAN-2.3.2 - úprava filtrů a dashboardů</td>
      <td>Major</td>
      <td>Reopened</td>
      <td>2018-02-19T13:10:35.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Sub-task</td>
      <td>RUIANADM-1194</td>
      <td>[RUIAN-2.3] Akceptace</td>
      <td>Minor</td>
      <td>In Progress</td>
      <td>2018-02-19T10:06:08.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Task</td>
      <td>CUZKRUIAN-18400</td>
      <td>BT20171020/32 - schválené BD zapsat do tabulky...</td>
      <td>Major</td>
      <td>Open</td>
      <td>2018-02-16T14:58:46.000+0100</td>
      <td>2018-03-09</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Task</td>
      <td>CUZKRUIAN-18391</td>
      <td>BT20171020/16 - [2.2. b)]  Uložit na PK do slo...</td>
      <td>Major</td>
      <td>Open</td>
      <td>2018-02-16T13:52:10.000+0100</td>
      <td>2017-11-20</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>118</th>
      <td>Task</td>
      <td>CUZKRUIAN-18387</td>
      <td>BT20171020/12 - Seznam úkolů zaslaných J.Vachu...</td>
      <td>Major</td>
      <td>Open</td>
      <td>2018-02-16T13:40:36.000+0100</td>
      <td>2017-11-30</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>119</th>
      <td>Task</td>
      <td>CUZKRUIAN-18386</td>
      <td>BT20171020/7 - S T.Holendou projednat bezp. testy</td>
      <td>Major</td>
      <td>Open</td>
      <td>2018-02-16T13:38:13.000+0100</td>
      <td>2017-11-10</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Bug</td>
      <td>RUIANADM-775</td>
      <td>Vykazování práce - řídící a režijní činnosti</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2018-02-09T00:57:03.000+0100</td>
      <td>None</td>
      <td>[Internal, Long_task]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Task</td>
      <td>RUIANADM-1303</td>
      <td>Objednávka služeb VersaSystems na rok 2018</td>
      <td>Minor</td>
      <td>In Progress</td>
      <td>2018-02-08T22:25:19.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Task</td>
      <td>RUIANADM-1305</td>
      <td>Objednávka služeb AutoCont na rok 2018</td>
      <td>Minor</td>
      <td>In Progress</td>
      <td>2018-02-08T21:57:38.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Task</td>
      <td>CUZKRUIAN-17986</td>
      <td>Nové GUI ISUI - režie</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2018-02-08T11:00:56.000+0100</td>
      <td>2019-04-30</td>
      <td>[Long_task]</td>
      <td>[xRUIAN-2.4.x (plán)]</td>
    </tr>
    <tr>
      <th>16</th>
      <td>New Feature</td>
      <td>RUIANADM-1221</td>
      <td>Dodávka RUIAN-2.4</td>
      <td>Major</td>
      <td>Open</td>
      <td>2018-02-07T12:56:53.000+0100</td>
      <td>2018-11-30</td>
      <td>[Long_task]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>222</th>
      <td>Sub-task</td>
      <td>CUZKRUIAN-3969</td>
      <td>odstraneni primeho volani DAO z FE ISUI</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2015-11-10T10:57:51.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-ENHANCEMENTS (Plán)]</td>
    </tr>
    <tr>
      <th>203</th>
      <td>Task</td>
      <td>CUZKRUIAN-15637</td>
      <td>Upravy buildu Java - odstranenit zavislost isk...</td>
      <td>Major</td>
      <td>Open</td>
      <td>2015-10-23T16:04:22.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>214</th>
      <td>Task</td>
      <td>CUZKRUIAN-7638</td>
      <td>Zpracování SDO_GEOMETRY</td>
      <td>Major</td>
      <td>Open</td>
      <td>2015-01-08T10:30:15.000+0100</td>
      <td>None</td>
      <td>[Internal, Refactoring]</td>
      <td>[xRUIAN-ENHANCEMENTS (Plán)]</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Task</td>
      <td>RUIANADM-453</td>
      <td>Úprava instalačního procesu na DEV a následně ...</td>
      <td>Major</td>
      <td>Need More Information</td>
      <td>2014-09-22T13:23:47.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>207</th>
      <td>Task</td>
      <td>CUZKRUIAN-12932</td>
      <td>Vyjasnění vztahu databází VDP a RUIAN</td>
      <td>Major</td>
      <td>Open</td>
      <td>2014-06-26T10:58:39.000+0200</td>
      <td>None</td>
      <td>[Internal]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>206</th>
      <td>Task</td>
      <td>CUZKRUIAN-14725</td>
      <td>Chybejici package TST_PACKAGE zpusobuje padani...</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2014-06-24T18:00:56.000+0200</td>
      <td>None</td>
      <td>[Internal]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>205</th>
      <td>Task</td>
      <td>CUZKRUIAN-14947</td>
      <td>Vytváření DB objektů v rámci integračních test...</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2014-06-23T16:59:42.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>217</th>
      <td>Improvement</td>
      <td>CUZKRUIAN-5468</td>
      <td>Sjednocení JPA anotací</td>
      <td>Minor</td>
      <td>In Progress</td>
      <td>2014-04-29T11:52:38.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-ENHANCEMENTS (Plán)]</td>
    </tr>
    <tr>
      <th>223</th>
      <td>Task</td>
      <td>CUZKRUIAN-3793</td>
      <td>Pridat do dokumentacie konfiguracie ISUI obmed...</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2014-04-09T14:04:10.000+0200</td>
      <td>None</td>
      <td>[Documentation, Internal]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>216</th>
      <td>Task</td>
      <td>CUZKRUIAN-5556</td>
      <td>Vyjasnit reference tříd do JPA konfig. souboru...</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2014-04-09T14:03:00.000+0200</td>
      <td>None</td>
      <td>[Internal]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>209</th>
      <td>Task</td>
      <td>CUZKRUIAN-12423</td>
      <td>init_ldev.cmd - doplnit kontroly na přítomnost...</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2014-04-09T13:58:24.000+0200</td>
      <td>None</td>
      <td>[Internal]</td>
      <td>[xRUIAN-ENHANCEMENTS (Plán)]</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Task</td>
      <td>RUIANADM-456</td>
      <td>Failed builds -&gt; JIRA issues</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2014-04-09T13:54:06.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Improvement</td>
      <td>RUIANADM-455</td>
      <td>prenaseni tabulkovych statistik na TEST</td>
      <td>Major</td>
      <td>Open</td>
      <td>2014-04-09T13:51:44.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Task</td>
      <td>RUIANADM-454</td>
      <td>Zavést politiku mazání starých tagů</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2014-04-09T13:33:04.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>215</th>
      <td>Improvement</td>
      <td>CUZKRUIAN-7604</td>
      <td>Zlepšit detekci COLLECTION typů</td>
      <td>Major</td>
      <td>Open</td>
      <td>2014-04-09T13:14:09.000+0200</td>
      <td>None</td>
      <td>[Internal]</td>
      <td>[xRUIAN-ENHANCEMENTS (Plán)]</td>
    </tr>
    <tr>
      <th>218</th>
      <td>Improvement</td>
      <td>CUZKRUIAN-5362</td>
      <td>Revidovat použití shared libraries pro konfigu...</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2014-02-04T11:55:30.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>97</th>
      <td>Task</td>
      <td>RUIANADM-399</td>
      <td>JIRA - zajistit, aby u implementačních tasků m...</td>
      <td>Major</td>
      <td>Open</td>
      <td>2014-02-03T13:57:40.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Bug</td>
      <td>RUIANADM-337</td>
      <td>Systematicky ošetřit propagaci DB oprav ze sta...</td>
      <td>Major</td>
      <td>Open</td>
      <td>2013-12-11T10:54:47.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>111</th>
      <td>New Feature</td>
      <td>PATCHMAN-72</td>
      <td>Automatizace aktualizace informací o prostředí...</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2013-11-11T11:10:53.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[2.0]</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Task</td>
      <td>RUIANADM-255</td>
      <td>hf.bat - řazení odkazů na skripty v _install.s...</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2013-10-02T09:52:07.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>101</th>
      <td>Task</td>
      <td>RUIANADM-253</td>
      <td>hf.bat - ignorovat neverzované skripty _g_path...</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2013-10-02T09:47:03.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>102</th>
      <td>Task</td>
      <td>RUIANADM-239</td>
      <td>Úpravy configuration / release managementu pro...</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2013-09-23T12:37:57.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Task</td>
      <td>RUIANADM-200</td>
      <td>metodika pro psaní UT na výrazně datově závisl...</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2013-08-20T12:11:37.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>212</th>
      <td>Improvement</td>
      <td>CUZKRUIAN-12348</td>
      <td>Vyčlenit AD_KONFIGURACE a spol. do samostatnéh...</td>
      <td>Major</td>
      <td>Open</td>
      <td>2013-08-20T09:35:41.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-ENHANCEMENTS (Plán)]</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Task</td>
      <td>RUIANADM-187</td>
      <td>Nainstalovat Oracle klienta na Jenkins server</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2013-08-07T09:54:17.000+0200</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>108</th>
      <td>Improvement</td>
      <td>RUIANADM-43</td>
      <td>utPLSQL testy - přidat formátování výsledků testů</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2013-03-18T15:20:54.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Bug</td>
      <td>RUIANADM-40</td>
      <td>build nenahrává data z mig_uir_m</td>
      <td>Major</td>
      <td>Open</td>
      <td>2013-03-14T10:31:38.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>213</th>
      <td>Improvement</td>
      <td>CUZKRUIAN-11824</td>
      <td>Zrychlenie generovania VF - pouzitie transform...</td>
      <td>Minor</td>
      <td>Open</td>
      <td>2013-02-08T13:32:08.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-ENHANCEMENTS (Plán)]</td>
    </tr>
    <tr>
      <th>211</th>
      <td>Task</td>
      <td>CUZKRUIAN-12378</td>
      <td>Modularizace DB částí systémů RUIAN</td>
      <td>Major</td>
      <td>Open</td>
      <td>2012-12-12T09:04:07.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-ENHANCEMENTS (Plán)]</td>
    </tr>
    <tr>
      <th>219</th>
      <td>Task</td>
      <td>CUZKRUIAN-5224</td>
      <td>Mapování DB view na  JPA Entity a "Structy"</td>
      <td>Major</td>
      <td>Open</td>
      <td>2012-12-06T13:35:11.000+0100</td>
      <td>None</td>
      <td>[]</td>
      <td>[xRUIAN-ENHANCEMENTS (Plán)]</td>
    </tr>
  </tbody>
</table>
<p>199 rows × 9 columns</p>
</div>




```python
#počet ticketů
print ("CUZKRUIANADM: ", [len(JT4[JT4['key'].str.contains('RUIANADM-')])])
print ("CUZKRUIAN: ", [len(JT4[JT4['key'].str.contains('RUIAN-')])])
print ("PATCHMAN: ", [len(JT4[JT4['key'].str.contains('PATCHMAN')])])
print ("Celkem: ", [len(JT4)])
```

    CUZKRUIANADM:  [85]
    CUZKRUIAN:  [113]
    PATCHMAN:  [1]
    Celkem:  [199]



```python
#jelikož jsem nepřišla na to, jak se v Jiře jmenuje "Security level", 
#tak není seřazeno dle Interní/externí" a tento sloupec také chybí
```


```python
JT4.to_csv('2018-04-05.csv', encoding='utf-8', index=False)
```
