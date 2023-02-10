$filepath = $args[0]
if (!(Test-Path -Path $args[0])) {
   throw "bib file not found"
}

$text = Get-Content -Path $args[0]
$text = $text -replace "ü", '\"{u}'
$text = $text -replace "ä", '\"{a}'
$text = $text -replace "ö", '\"{o}'
$text = $text -replace "č", '\v{c}'
$text = $text -replace "é", "\'{e}"
$text = $text -replace "á", "\'{a}"

$text | Set-Content -Path $args[0]

