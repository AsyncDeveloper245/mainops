pipeline {
  
  
  agent any
  
  stages{
  
        stage("build frontend/client"){
          
          steps{
          sh "cd client && npm ci --force"

            
          }
        }
    
          
          stage("deploy code"){
            
            steps{
          
           sh "sudo cp -rf client /home/azureuser/"
           sh "sudo cp -rf backend /home/azureuser/"
           sh "pm2 start npm -- start --prefix /home/azureuser/client"
          
            }
          }
  
  
  
  }




}
