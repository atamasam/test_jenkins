pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Code aus dem GitHub-Repository auschecken
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // Installiere Abhängigkeiten (z.B. unittest ist standardmäßig in Python enthalten)
                sh 'echo "Dependencies installation step here, e.g., pip install"'
            }
        }
        stage('Run Tests') {
            steps {
                // Führe die Unit-Tests aus
                sh 'python3 -m unittest test_game.py'
            }
        }
    }
}
