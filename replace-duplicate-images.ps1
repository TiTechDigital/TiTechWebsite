# Replace duplicate partner images with diverse new images across the site

$imageMap = @{
    'partner-01' = 'about'
    'partner-02' = 'services'
    'partner-03' = 'industries'
    'partner-04' = 'contact'
    'partner-05' = 'tools'
    'partner-06' = 'work'
}

Write-Host "Replacing duplicate images..." -ForegroundColor Cyan

$htmlFiles = Get-ChildItem -Path . -Filter "*.html" -Recurse -Exclude "404.html","og-card.html","brand-logo.html","*.original.html"

$count = 0
foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    
    foreach ($oldImg in $imageMap.Keys) {
        $newImg = $imageMap[$oldImg]
        $content = $content -replace "$oldImg-480\.webp", "$newImg-480.webp"
        $content = $content -replace "$oldImg-720\.webp", "$newImg-720.webp"
        $content = $content -replace "$oldImg-900\.webp", "$newImg-900.webp"
    }
    
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -NoNewline -Encoding UTF8
        $count++
        Write-Host "Updated: $($file.Name)"
    }
}

Write-Host "Total files updated: $count" -ForegroundColor Green
