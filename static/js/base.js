// functions for budget calculator
var total=0
function calculateBudget(p1, p2, p3, p4){
    var a=document.getElementById(p1).value;
    var b=document.getElementById(p2).value;
    var c=document.getElementById(p3).value;
    var d=document.getElementById(p4).value;
    total=Number(a)+Number(b)+Number(c)+Number(d);
    document.getElementById("result").innerHTML = total;
}

function compareBudgetWithCost(budg, destination){
    var userBudget=document.getElementById(budg).value;
    var budgetResult;
    if (userBudget == 0){
        budgetResult = "Please insert a bugdet!";
    } else if (total ==  0){
        budgetResult = "Please fill in the travel costs!";
    } else if (userBudget >= total){
        budgetResult = "You have enought money for this trip!";
    } else {
        budgetResult = "Your budget is to low!";
    }
    document.getElementById("finalResult").innerHTML = budgetResult;
}

