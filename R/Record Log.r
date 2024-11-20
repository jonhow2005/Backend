"Options:"
"New Record/ Acsess Log/ Clear"
resp <- readline("")
Array1 <- list("--")
Array2 <- list("--")
Array3 <- list("----")
LogArray <- list("\n")

New_Record <- function(){
Data1 <- scan("Scan Day")
Data2 <- scan("Scan Month")
Data3 <- scan("Scan Year")
Record <- readline("Enter Log")

Array1 <- append(Array1, Data1)
Array2 <- append(Array2, Data2)
Array3 <- append(Array3, Data3)
LogArray <- append(LogArray, Record)
}

Acsess_Log <- function(){
for (x in LogArray) {
  print(paste(Array1[x],"/",Array2[x],"/",Array3[x]))
  print(LogArray[x])
}
}

Clear <- function(){
  cat("/014")
}

if (resp = "Clear") {
  Clear()
}else if (resp = "New Record"){
  New_Record()
}

else if (resp = "Acsess Log"){
  Acsess_Log()
}
  
