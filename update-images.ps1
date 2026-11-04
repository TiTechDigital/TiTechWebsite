# Script to update HTML files to use different images per section

$imageMapping = @{
    # Homepage
    'index.html' = 'hero-home'
    'en/index.html' = 'hero-home'
    
    # Services
    'servizi' = 'services'
    'en/services' = 'services'
    
    # Blog
    'blog' = 'blog'
    'en/blog' = 'blog'
    
    # Tools
    'strumenti' = 'tools'
    'en/tools' = 'tools'
    
    # Industries
    'settori' = 'industries'
    'en/industries' = 'industries'
    
    # Work/Portfolio
    'lavori' = 'work'
    'en/work' = 'work'
    
    # Contact
    'contatti' = 'contact'
    'en/contact' = 'contact'
    
    # About/How we work
    'chi-siamo' = 'about'
    'come-lavoriamo' = 'about'
    'en/about' = 'about'
    'en/how-we-work' = 'about'
    
    # Legal pages (use contact image)
    'privacy' = 'contact'
    'cookie' = 'contact'
    'en/privacy' = 'contact'
    'en/cookies' = 'contact'
}

function Get-ImageForPath {
    param($filePath)
    
    $path = $filePath.Replace('\', '/')
    
    # Check specific matches first (more specific to less specific)
    if ($path -match '(en/)?services/') { return 'services' }
    if ($path -match '(en/)?blog/') { return 'blog' }
    if ($path -match '(en/)?tools/') { return 'tools' }
    if ($path -match '(en/)?industries/') { return 'industries' }
    if ($path -match '(en/)?work/') { return 'work' }
    if ($path -match '(en/)?contact/') { return 'contact' }
    if ($path -match '(en/)?about/') { return 'about' }
    if ($path -match '(en/)?how-we-work/') { return 'about' }
    if ($path -match 'servizi/') { return 'services' }
    if ($path -match 'strumenti/') { return 'tools' }
    if ($path -match 'settori/') { return 'industries' }
    if ($path -match 'lavori/') { return 'work' }
    if ($path -match 'contatti/') { return 'contact' }
    if ($path -match 'chi-siamo/') { return 'about' }
    if ($path -match 'come-lavoriamo/') { return 'about' }
    if ($path -match '(en/)?privacy/') { return 'contact' }
    if ($path -match '(en/)?cookie') { return 'contact' }
    if ($path -match '(en/)?index\.html$') { return 'hero-home' }
    
    return 'hero-home' # Default
}

$htmlFiles = Get-ChildItem -Path . -Filter "*.html" -Recurse -Exclude "404.html","og-card.html","brand-logo.html","*.original.html"

$count = 0
foreach ($file in $htmlFiles) {
    $imageName = Get-ImageForPath $file.FullName
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    
    # Replace hero images in main content (NOT in preload or footer)
    # Update hero section images
    $content = $content -replace '(<div class="hero__stage".*?<img class="hero__img" src=")([^"]*hero-\d+\.webp)', "`${1}assets/img/$imageName-700.webp"
    $content = $content -replace '(srcset=")([^"]*hero-700\.webp \d+w, )([^"]*hero-1400\.webp)', "`${1}assets/img/$imageName-700.webp 700w, assets/img/$imageName-1400.webp"
    
    # Update aperture/period images in hero
    $content = $content -replace '(<span class="hero__aperture"><img class="hero__img" src=")([^"]*hero-\d+\.webp)', "`${1}assets/img/$imageName-700.webp"
    
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -NoNewline -Encoding UTF8
        $count++
        Write-Host "Updated: $($file.FullName) -> $imageName"
    }
}

Write-Host "`nTotal files updated: $count" -ForegroundColor Green
