pipeline {
    agent any
    environment {
        DEVELOPER = 'develop'
        BRANCH = "${BRANCH_NAME}" 
        ANSIBLE_FORCE_COLOR = 'true'
    }

    stages {
        stage('Get branch name') {
            steps {
                script {
                    branch = env.BRANCH
                }
            }
        }
    
        stage('Automation Process') {
            steps {
                powershell '''
                    Set-Location -Path "C:\\User\\aslim\\.jenkins\\workspace\\qa_pipeline"
                    Write-Output "Automation process running..."
                    python -m pip install -r requirements.txt
                    Get-Location
                '''
            }
        }
    }
}
