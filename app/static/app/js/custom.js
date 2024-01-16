const PrintButton = document.getElementById('print-button');
const PrintPage = () =>{
    const printFrame = document.createElement('iframe');
    printFrame.style.display='none'; 
    printFrame.src="D:\FondationB\Banza\Dany\templates\fiche.html";
    document.body.appendChild(printFrame);
    printFrame.contentWindow.focus();
    printFrame.contentWindow.print();

};
PrintButton.addEventListener('click', () => {
    PrintPage();

})
