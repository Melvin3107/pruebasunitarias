pipeline {
    agent any

    stages {
        stage('Verificar Instalación') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }

        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/Melvin3107/pruebasunitarias.git', branch: 'main'
            }
        }

        stage('Crear Entorno Virtual') {
            steps {
                sh 'python3 -m venv venv'
            }
        }

        stage('Activar Entorno Virtual y Instalar Dependencias') {
            steps {
                sh './venv/Scripts/pip install -r requirements.txt'
            }
        }

        stage('Ejecutar Pruebas matematicas') {
            steps {
                sh './venv/Scripts/python app.py'
            }
        }
    }

    post {
        success {
            echo 'Las pruebas se ejecutaron correctamente.'
        }
        failure {
            echo 'Una o más pruebas fallaron.'
        }
    }
}
