const prompt= require("prompt-sync")()

const ROWS=3
const COLS=3

const SYMBOLS_COUNT={
    "A":2,
    "B":4,
    "C":6,
    "D":8    
}
const SYMBOLS_VALUE={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

const getdeposit=() => {
    while(true){

    
        const amountDeposited= prompt("Enter the amount ot be deposited: ")
        const numberDeposited= parseFloat(amountDeposited)
        if (isNaN(numberDeposited) || numberDeposited <=0){
            console.log("Invalid resposne! Try again.")
        }
        else {
            return numberDeposited;
        }
    }
}

const getumberOfLines=() =>{
    while(true){
        const lines=prompt("Enter the number of lines (1-3): ")
        const numberOfLines=parseFloat(lines)
        if(isNaN(numberOfLines) || numberOfLines<=0 || numberOfLines>3){
            console.log("Invalid response! Choose lines in the range (1-3)")
        }
        else{
            return numberOfLines
        }
    }
}



const getBetamout=(balance,lines)=>{
    while(true){
        const bet= prompt("Enter a bet amount per line: ")
        const betAmount=parseFloat(bet)
        if(isNaN(betAmount)|| betAmount > balance/lines){
            console.log("Invalid amount! Try Again")
        }
        else{
            return betAmount
        }
    }
}

const spin=()=>{
    const symbols=[]
    for (const [symbol,count] of Object.entries(SYMBOLS_COUNT)){
        for (let i=0;i<count;i++){
            symbols.push(symbol)
        }
    } 
    const reels=[]
    for (let i=0;i<COLS;i++){
        reels.push([])
        const reelSymbols=[...symbols]
        for (let j=0;j<ROWS;j++){
            const randomIndex=Math.floor(Math.random()*reelSymbols.length)
            const selectedSymbol= reelSymbols[randomIndex]
            reels[i].push(selectedSymbol)
            reelSymbols.splice(randomIndex,1)
        }
    }
    //console.log(reels)
    return reels
}

const transpose=(reels)=>{
    const trans=[]
    for (let i=0;i<ROWS;i++){
        trans.push([])
        for (let j=0;j<COLS;j++){
            trans[i].push(reels[j][i])
        }
    }
    //console.log(trans)
    return trans

}

const printTrans=(trans)=>{
    for (row of trans){
        let rowString=""
        for ([i,symbol] of row.entries()){
            rowString+=symbol
            if(i!=row.length){
                rowString+= " | "
            }
        }
    console.log(rowString)
    }
    
}
const checkWin=(trans,numberOfLines,bet)=>{
    let winnings=0
    for(let row=0;row<numberOfLines;row++){
        const symbols=trans[row]
        let allSame= true
        for (const symbol of symbols){
            if (symbol!=symbols[0]){
                allSame=false
                break
            }
        }
        if(allSame){
            winnings=bet*SYMBOLS_VALUE[symbols[0]]
        }
    
    }
    return winnings

}

const game=()=>{
    let balance= getdeposit()

    while(true){
        console.log("You have a balance of $ "+ balance)
        const numberOfLines=getumberOfLines()
        const bet=getBetamout(balance,numberOfLines)
        balance-=bet*numberOfLines
        const reels=spin()
        const trans=transpose(reels)
        printTrans(trans)
        const winnings=checkWin(trans,numberOfLines,bet)
        balance+=winnings
        console.log("You won $" + winnings)
        if (balance <=0){
            console.log("You ran out of money!")
            break
        }
        const playAgain=prompt("Do you wanna play again (y/n)?")
        if (playAgain!="y"){
            break
        }

    }
    
}

game()