pipeline {
    agent any
    envirement {
        DEVELOPER = 'develop'
        BRANCH = '${BRANCH_NAME}' 
        ANSIBLE_FORCE_COLOR = 'true'

    }

    stages{
        stage('Get branch name'){
            steps{
                script {
                    branch = env.BRANCH
                }
            }
        }
    }

        stage('Automation Process'){
            script{
                dir('/User/aslim/.jenkins/workspace/qa_pipeline'){
                    echo 'Automation process running...'
                        sh 'pip3 install -r requirements.txt'
                        sh 'pwd'
                }
            }
        }

        post {
            always {
                echo 'Automation process finished...'
            }
        }

}