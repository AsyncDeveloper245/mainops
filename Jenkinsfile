pipeline {

  stages{
  
        stage("build frontend"){
          
          steps{
          sh "cd client"
          sh "npm install"
          sh "npm run build"
            
          }
        }
    
//     stage("build backend){
//            sh ""
          
//           }
          
          
          stage("deploy code"){
            
            steps{
          
           sh "cp -rf client /home/azureuser/frontend"
           sh "cp -rf backend /home/azureuser/backend"
           sh "cd /home/azureuser/frontend  && pm2 server build"
          
            }
          }
  
  
  
  }




}
