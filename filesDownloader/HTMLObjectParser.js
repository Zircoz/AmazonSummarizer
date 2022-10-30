/*
1. Either right click on the table of list of files and click Inspect
 OR
1. Go to this XPath: /html/body/div[1]/div[2]/div[1]/div/table/tbody

2. Right click on the tbody element and click "use in console". A new object in console will be created, assign it to `rows` then run the following code in console.
*/

//rows=temp0
const parser = new DOMParser();
for (let step = 1; step < 5; step++) {
  strInnerHTML = rows.children[step].children[2].innerHTML;
  innerHTMLtemp = parser.parseFromString(strInnerHTML, "text/html");
  downloadURL = innerHTMLtemp.getElementsByTagName("a")[0].href;
  window.open(downloadURL);
}

/* 
Right click on output of command and select copy whole object, paste it to the object.json file.
*/
