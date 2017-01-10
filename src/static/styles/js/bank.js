function demo1(link1) {

	var resultdiv = document.getElementById("Verification Result")

	resultdiv.innerHTML = "";

    setTimeout(function(){

    	setTimeout(function(){
			document.getElementById("link1").innerHTML = '<a href="' + link1 + '"a>' + link1 + '</a>';
       		document.getElementById("status1").innerHTML = "Verified";
    	}, 1000);

       	resultdiv.innerHTML = resultdiv.innerHTML + '<p> Verification done by HSBC found! </p>';
    }, 3000);
    resultdiv.innerHTML = resultdiv.innerHTML + '<p> Looking up on block chain </p>';

}


function demo2(link2) {

	var resultdiv = document.getElementById("Verification Result")

	resultdiv.innerHTML = "";

    setTimeout(function(){

    	setTimeout(function(){

    		setTimeout(function(){

    			setTimeout(function(){

    			setTimeout(function(){
					document.getElementById("link2").innerHTML = '<a href="' + link2 + '"a>' + link2 	 + '</a>';
		       		document.getElementById("status2").innerHTML = "Verified";
	    			}, 1000);
    				resultdiv.innerHTML = resultdiv.innerHTML + '<p> Verification by BOA added to blockchain </p>';
	    		}, 3000);
       			resultdiv.innerHTML = resultdiv.innerHTML + '<p> Compliance cleared, submit to block chain now </p>';
    		}, 3000);
       		resultdiv.innerHTML = resultdiv.innerHTML + '<p> Verifying with KYC compliance </p>';
    	}, 3000);
       	resultdiv.innerHTML = resultdiv.innerHTML + '<p> Verification not found on block chain </p>';
    }, 3000);
    resultdiv.innerHTML = resultdiv.innerHTML + '<p> Looking up on block chain </p>';

}
