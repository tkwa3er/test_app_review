/*const {exec}=require('child_process')
const vscode=require('vscode')
function activate(context){
	
    let disposable= vscode.commands.registerCommand('runMyScript',function(){
        exec('bash myGen.sh',(error,stdout,stderr)=>{
            if(error)
            {
                console.error('exec error: ${error]');
                
                return;
            }
            console.log('stdout: ${stdout}');
            console.log('stderr: ${stderr}');

        });
    });
    context.subscriptions.push(disposable);

}
exports.activate=activate;*/
const execShell = (cmd: string) =>
    new Promise<string>((resolve, reject) => {
      cp.exec(cmd, (err, out) => {
        if (err) {
          return resolve(cmd+' error!');
          //or,  reject(err);
        }
        return resolve(out);
      });
    });

  //... show powershell output from 'pwd'...
  context.subscriptions.push(
    vscode.commands.registerCommand('test', async () => {
      const output = await execShell('powershell pwd');
      vscode.window.showInformationMessage(output);
    })
  );
