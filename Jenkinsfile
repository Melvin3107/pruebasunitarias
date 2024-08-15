pipeline {
    agent any

    stages {
        stage('Verificar Instalación') {
            steps {
                bat 'python --version'
                bat 'pip --version'
            }
        }

        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/Melvin3107/pruebasunitarias.git', branch: 'main'
            }
        }

        stage('Crear Entorno Virtual') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Activar Entorno Virtual y Instalar Dependencias') {
            steps {
                bat '.\\venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                bat '.\\venv\\Scripts\\python run_tests.py'
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
