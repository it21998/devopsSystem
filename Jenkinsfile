pipeline {
    agent any


    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'main', url: 'https://github.com/it21998/devopsSystem.git'

                
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    python3 -m venv myvenv
                    source myvenv/bin/activate
                    pip install -r requirements.txt
                    cd student_management
                    cp student_management/.env.example student_management/.env
                    ./manage.py test'''
            }
        }
        
    
        stage('deploym to vm 1') {
            steps{
                sshagent (credentials: ['ssh-deploy']) {
                    sh '''
                        ansible-playbook -i ~/workspace/ansible-project/ansible-example-jenkins/hosts.yml -l deploymentjenkins ~/workspace/ansible-project/ansible-example-jenkins/playbooks/django2-install.yml
                    '''
                }

            }

        }
    }
}
