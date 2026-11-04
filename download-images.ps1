# PowerShell script to download professional tech images from Unsplash
# Run this script to automatically download all images

$images = @(
    @{
        Name = "hero-home"
        Url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1400&q=85"
        Description = "Technology/Space - Homepage hero"
    },
    @{
        Name = "services"
        Url = "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1400&q=85"
        Description = "Laptop coding - Services pages"
    },
    @{
        Name = "blog"
        Url = "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1400&q=85"
        Description = "Work desk - Blog pages"
    },
    @{
        Name = "tools"
        Url = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1400&q=85"
        Description = "Data charts - Tools/Calculators"
    },
    @{
        Name = "industries"
        Url = "https://images.unsplash.com/photo-1565514020179-026b92b84bb6?w=1400&q=85"
        Description = "Factory/Industrial - Industries pages"
    },
    @{
        Name = "work"
        Url = "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=1400&q=85"
        Description = "Web design - Work/Portfolio"
    },
    @{
        Name = "contact"
        Url = "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=1400&q=85"
        Description = "Network - Contact pages"
    },
    @{
        Name = "about"
        Url = "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1400&q=85"
        Description = "Modern office - About pages"
    }
)

Write-Host "Downloading professional tech images from Unsplash..." -ForegroundColor Cyan
Write-Host "These images are free to use under the Unsplash License" -ForegroundColor Green
Write-Host ""

$outputDir = "assets/img"
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

foreach ($img in $images) {
    Write-Host "Downloading: $($img.Description)" -ForegroundColor Yellow
    
    # Download 1400px version
    $output1400 = Join-Path $outputDir "$($img.Name)-1400.webp"
    try {
        Invoke-WebRequest -Uri $img.Url -OutFile $output1400 -UseBasicParsing
        Write-Host "  ✓ Downloaded $($img.Name)-1400.webp" -ForegroundColor Green
    } catch {
        Write-Host "  ✗ Failed to download 1400px version: $_" -ForegroundColor Red
    }
    
    # Download 700px version (modify URL)
    $url700 = $img.Url -replace 'w=1400', 'w=700'
    $output700 = Join-Path $outputDir "$($img.Name)-700.webp"
    try {
        Invoke-WebRequest -Uri $url700 -OutFile $output700 -UseBasicParsing
        Write-Host "  ✓ Downloaded $($img.Name)-700.webp" -ForegroundColor Green
    } catch {
        Write-Host "  ✗ Failed to download 700px version: $_" -ForegroundColor Red
    }
    
    Write-Host ""
}

Write-Host "Download complete!" -ForegroundColor Cyan
Write-Host "Images saved to: $outputDir" -ForegroundColor Green
Write-Host ""
Write-Host "Note: These images are from Unsplash and are free to use commercially." -ForegroundColor Yellow
Write-Host "License: https://unsplash.com/license" -ForegroundColor Yellow
