# Set your GitHub organization name and personal access token
$organization = "CloudiFyi-Solutions"
$accessToken = "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"

# Set the destination directory where repositories will be cloned
$destinationDirectory = "/Users/shahrukh/Documents/CloudiFyi repos"

# Authenticate with your personal access token
$headers = @{
    "Authorization" = "Bearer $accessToken"
    "Accept" = "application/vnd.github.v3+json"
}

# Get the list of repositories in the organization
$url = "https://api.github.com/orgs/$organization/repos"
$repositories = Invoke-RestMethod -Uri $url -Headers $headers

# Iterate through each repository and clone it
foreach ($repo in $repositories) {
    $repoName = $repo.name
    $repoUrl = $repo.clone_url
    $repoDirectory = Join-Path -Path $destinationDirectory -ChildPath $repoName
    
    # Clone the repository using Git
    Write-Host "Cloning repository: $repoName"
    git clone $repoUrl $repoDirectory
}

Write-Host "All repositories cloned successfully."
