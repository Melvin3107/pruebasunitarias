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
                // Activar entorno virtual y usar pip para instalar dependencias
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                // Activar entorno virtual y ejecutar pruebas
                sh '''
                . venv/bin/activate
                python -m unittest discover
                '''
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
        always {
            // Limpiar el workspace después de la ejecución del pipeline
            deleteDir()
        }
    }
}
