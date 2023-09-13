const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})


const question = async () => {
  return new Promise((resolve, reject) => {
    rl.question("Masukkan baris : ", (data) => {
      resolve(data)
    })
  })
}

let baris
async function stars() {
  let data = await question()
  for(let i = 0; i < data; i++) {
    let spasi = " ".repeat(data-i)
    let bin = "*".repeat(2*i+1)
    console.log(spasi + bin)
    rl.close()
  }
}


stars()



