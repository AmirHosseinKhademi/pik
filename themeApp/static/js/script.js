	/*
	This file contains the main js functions
	Author : Not mentioned since FANAVARD's rules. 
	Date : 7/8/94
	*/
	
	
	/* This Function Prevents Forms to Refresh the Page or Redirect to Another Page (Since we Need to Print Some Messages via JS in the Site Demo) */
	$("#form").submit(function(e) {
    e.preventDefault();
	});
	
	/* This Function Prevents Forms to Refresh the Page or Redirect to Another Page (Since we Need to Print Some Messages via JS in the Site Demo) */
	$("#checkout-form").submit(function(e) {
    e.preventDefault();
	});
	
	/* This Function Prevents Forms to Refresh the Page or Redirect to Another Page (Since we Need to Print Some Messages via JS in the Site Demo) */
	$("#charge-form").submit(function(e) {
    e.preventDefault();
	});
	
	/* This Function will Print a Message after Submiting a Form */
	function createGruoupMessage() {
		document.getElementById("msg").style.display = "block" ;
		document.getElementById("msg").innerHTML = "گروه با موفقیت ایجاد شد ." ;
	}
	
	/* This Function will Print a Message after Submiting a Form */
	function addPurchaseMessage() {
		document.getElementById("msg").style.display = "block" ;
		document.getElementById("msg").innerHTML = "خرید با موفقیت ایجاد شد و هم اکنون از طریق بخش خرید ها در دسترس است ." ;
	}
	
	/* This Function will Simulate Account Charging */	
	function chargeAccount() {
		var ca = document.getElementById("charge-amount").value ;
		var ab = document.getElementById("account-balance").innerHTML ;
		var Numca = ca*1 ;
		var Numab = ab*1 ;
		document.getElementById("account-balance").innerHTML = Numca + Numab ;	
		document.getElementById("msg").style.display = "block" ;
		document.getElementById("msg").innerHTML = "حساب شما با موفقیت شارژ شد ." ;
	}

	/* This Function will Print a Message after Submiting a Form */	
	function CheckoutMessage() {
		document.getElementById("CheckoutMessage").style.display = "block" ;
		document.getElementById("CheckoutMessage").innerHTML = "درخواست تسویه حساب شما ثبت شد ." ;
	}
	
	/* This Function will Print a Message after Submiting a Form */
	function updateProfileMessage() {
		document.getElementById("msg").style.display = "block" ;
		document.getElementById("msg").innerHTML = "پروفایل شما بروز شد ." ;
	}
	
	/* This Function will Print a Message after Submiting a Form */
	function resendReciptionMailMessage(){
		document.getElementById("msg").style.display = "block" ;
		document.getElementById("msg").innerHTML = "فاکتور خرید به آدرس ایمیل شما ارسال شد ." ;
	}
	
	/* This Function Filter the Results in Purchases Page */
	function filterAll(){
		document.getElementById("purchase-box-01").style.display = "block" ;
		document.getElementById("purchase-box-02").style.display = "block" ;
		document.getElementById("purchase-box-03").style.display = "block" ;
		document.getElementById("purchase-box-04").style.display = "block" ;
		document.getElementById("filter-all").style.background = "rgb(96, 34, 132)" ;
		document.getElementById("filter-dabirestan").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-coworkers").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-mountain").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-reza-hossein").style.background = "rgba(96, 34, 132, 0.55)" ;		
	}
	
	/* This Function Filter the Results in Purchases Page */
	function filterDabirestan(){
		document.getElementById("purchase-box-01").style.display = "block" ;
		document.getElementById("purchase-box-02").style.display = "none" ;
		document.getElementById("purchase-box-03").style.display = "none" ;
		document.getElementById("purchase-box-04").style.display = "block" ;
		document.getElementById("filter-all").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-dabirestan").style.background = "rgb(96, 34, 132)" ;
		document.getElementById("filter-coworkers").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-mountain").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-reza-hossein").style.background = "rgba(96, 34, 132, 0.55)" ;		
	}

	/* This Function Filter the Results in Purchases Page */
	function filterCoworkers(){
		document.getElementById("purchase-box-01").style.display = "none" ;
		document.getElementById("purchase-box-02").style.display = "none" ;
		document.getElementById("purchase-box-03").style.display = "none" ;
		document.getElementById("purchase-box-04").style.display = "block" ;
		document.getElementById("filter-all").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-dabirestan").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-coworkers").style.background = "rgb(96, 34, 132)" ;
		document.getElementById("filter-mountain").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-reza-hossein").style.background = "rgba(96, 34, 132, 0.55)" ;		
	}

	/* This Function Filter the Results in Purchases Page */
	function filterMountain(){
		document.getElementById("purchase-box-01").style.display = "block" ;
		document.getElementById("purchase-box-02").style.display = "block" ;
		document.getElementById("purchase-box-03").style.display = "none" ;
		document.getElementById("purchase-box-04").style.display = "none" ;
		document.getElementById("filter-all").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-dabirestan").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-coworkers").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-mountain").style.background = "rgb(96, 34, 132)" ;
		document.getElementById("filter-reza-hossein").style.background = "rgba(96, 34, 132, 0.55)" ;		
	}

	/* This Function Filter the Results in Purchases Page */
	function filterRezaHossein(){
		document.getElementById("purchase-box-01").style.display = "block" ;
		document.getElementById("purchase-box-02").style.display = "none" ;
		document.getElementById("purchase-box-03").style.display = "none" ;
		document.getElementById("purchase-box-04").style.display = "none" ;
		document.getElementById("filter-all").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-dabirestan").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-coworkers").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-mountain").style.background = "rgba(96, 34, 132, 0.55)" ;
		document.getElementById("filter-reza-hossein").style.background = "rgb(96, 34, 132)" ;		
	}	

	/* Simulate the Payment */
	function picPayment01() {
		document.getElementById("account-balance").innerHTML -= 13500 ;
		if	(document.getElementById("account-balance").innerHTML>=0) {
			document.getElementById("account-balance").style.color="#8AB928";
		}	else {
			document.getElementById("account-balance").style.color="#C42A2E";
		}
	}

	/* Simulate the Payment */	
	function picPayment02() {
		document.getElementById("account-balance").innerHTML -= 22000 ;
		if	(document.getElementById("account-balance").innerHTML>=0) {
			document.getElementById("account-balance").style.color="#8AB928";
		}	else {
			document.getElementById("account-balance").style.color="#C42A2E";
		}
	}

	/* Simulate the Payment */
	function picPayment03() {
		document.getElementById("account-balance").innerHTML -= 5000 ;
		if	(document.getElementById("account-balance").innerHTML>=0) {
			document.getElementById("account-balance").style.color="#8AB928";
		}	else {
			document.getElementById("account-balance").style.color="#C42A2E";
		}
	}
	
	/* Simulate the Payment */	
	function picPayment04() {
		document.getElementById("account-balance").innerHTML -= 7200 ;
		if	(document.getElementById("account-balance").innerHTML>=0) {
			document.getElementById("account-balance").style.color="#8AB928";
		}	else {
			document.getElementById("account-balance").style.color="#C42A2E";
		}
	}	
	
	/* Simulate Remove an Added Member - in Create Group Page  */
	function hideMember01() {
		document.getElementById("Member01").style.display = "none" ;
	}
	
	/* Simulate Remove an Added Member - in Create Group Page  */
	function hideMember02() {
		document.getElementById("Member02").style.display = "none" ;
	}	
	
	/* Simulate Remove an Added Member - in Create Group Page  */
	function hideMember03() {
		document.getElementById("Member03").style.display = "none" ;
	}

	/* Simulate Remove an Added Member - in Create Group Page  */
	function hideMember04() {
		document.getElementById("Member04").style.display = "none" ;
	}	