

function toLogin(login, password) {
  if (login == "Bart") {
    if (password == "aft123") {
      console.log("Bienvenido a Springfield");
    } else {
      console.log("Contraseña incorrecta");
    }
  } else {
    console.log("No puedes entrar en la ciudad");
  }
}



function toLoginRefactor(login, password) {
  if (login != "Bart")
    return console.log("No puedes entrar en la ciudad");

  if (password != "aft123")
    return console.log("Contraseña incorrecta");

  console.log("Bienvenido a Springfield");
}

console.log("Correct -----------------------------------------------------");
toLogin("Bart", "aft123");
toLoginRefactor("Bart", "aft123");

console.log("Incorrect password -----------------------------------------------------");
toLogin("Bart", "123");
toLoginRefactor("Bart", "123");

console.log("Icorrect User -----------------------------------------------------");

toLogin("art", "123");
toLoginRefactor("art", "123");