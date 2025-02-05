let element = document.getElementById("book-details")

let book = localStorage.getItem("selectedBook");

const categoriesStorage = localStorage.getItem('categories');
const newCategories = JSON.parse(categoriesStorage);
const booksStorage = localStorage.getItem('books');
const newBooks = JSON.parse(booksStorage);




