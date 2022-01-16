pipeline {
    agent any
    environment { 
        PROJECT_NAME = "Pomidorchik"
        OWNER_NAME = "Nastya K"
    }
    stages {
        stage('Сборка') {
            steps {
                echo 'Выполняем команды для сборки'
                echo "Hello ${OWNER_NAME} its ${PROJECT_NAME}"
            }
        }
        stage('Тестирование') {
            steps {
                echo 'Тестируем нашу сборку'
            }
        }
        stage('Развертывание') {
            steps {
                echo 'Переносим код в рабочую среду или создаем артефакт'
            }
        }
    }
}
