pipeline {
    agent any
    environment {
        DEVELOPER = 'develop'
        BRANCH = "${BRANCH_NAME}" 
        ANSIBLE_FORCE_COLOR = 'true'
        REQUIREMENTS_FILE_PATH = "C:\\Users\\aslim\\OneDrive\\Belgeler\\GitHub\\qa_bootcamp_test_case\\tests\\requirements.txt"
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
                    Set-Location -Path "C:\\Users\\aslim\\OneDrive\\Belgeler\\GitHub\\qa_bootcamp_test_case\\tests"
                    Write-Output "Automation process running..."
                    python -m pip install -r $env:REQUIREMENTS_FILE_PATH
                    Get-Location
                '''
            }
        }
    }
}
