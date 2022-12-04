pipeline {
  
  
  agent any
  
  stages{
  
        stage("build frontend/client"){
          
          steps{
          sh "cd client && npm install --force && npm run build"

            
          }
        }
    
          
          stage("deploy code"){
            
            steps{
          
           sh "cp -rf client /home/azureuser/frontend"
           sh "cp -rf backend /home/azureuser/backend"
           sh "cd /home/azureuser/frontend  && pm2 server build"
          
            }
          }
  
  
  
  }




}
