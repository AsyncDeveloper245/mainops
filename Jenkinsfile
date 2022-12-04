pipeline {

  stages{
  
        steps("build frontend"){
          sh "cd client"
          sh "npm install"
          sh "npm run build"
        }
    
//     stage("build backend){
//            sh ""
          
//           }
          
          
          steps("deploy code"){
          
           sh "cp -rf client /home/azureuser/frontend"
           sh "cp -rf backend /home/azureuser/backend"
           sh "cd /home/azureuser/frontend  && pm2 server build"
          
          }
  
  
  
  }




}
