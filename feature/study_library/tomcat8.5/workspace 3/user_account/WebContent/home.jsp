<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>Feedbap</title>

<style type="text/css">
* {
	margin: 0px;
	padding: 0px;
}

header {
  height: 180px;
  text-align: center;

}
header h1 a {
  text-decoration: none;
  letter-spacing: 10px;
  color: black;

}
nav ul {
  list-style: none;
  text-align: center;

  
  padding: 10px 0;
}
nav ul li {
  display: inline;
  padding: 0 10px;
  letter-spacing: 10px;
}
nav ul li a{
  text-decoration: none;
}
nav ul li a:hover {
  text-decoration: none;
}
</style>

</head>
<body>
	<header>
	<h1><a href="home.jsp"><img src="image/feedbapLogo.png" height=200px></a></h1></h1>
	 
	</header>
	<nav>
		<ul>
		<%if (session.getAttribute("name")==null){
			
			System.out.println("11111");%>
			<li><a target="iframe1" href=category/list_user.jsp>HOME</a></li>
			<li><a target="iframe1" href=login_logout/login.jsp>LOGIN</a></li>
	
			<li><a target="iframe1" href=login_logout/registration.jsp>SIGN UP</a></li>
			<li><a target="iframe1" href=category/customize.jsp>CUSTOMIZE</a></li>
			<li><a target="iframe1" href=category/about.jsp>ABOUT</a></li>
			<li><a target="iframe1" href=category/production.jsp>PRODUCTION</a></li>
			<li><a target="iframe1" href=category/faq.jsp>FAQ</a></li>

			<li><a target="iframe1" href=category/contact.jsp>CONTACT</a></li>
			
			
		</ul>
		<%} 
		else {
			System.out.println("222221");%>
		
		<li><%=session.getAttribute("name").toString() + "님 안녕하세요!" %></li>
			<li><a target="iframe1" href=category/list_user.jsp>HOME</a></li>
			<li><a href=login_logout/logout.jsp>LOGOUT</a></li>
			<li><a target="iframe1" href=login_logout/mypage.jsp>MYPAGE</a></li>
			<li><a href=login_logout/customize.jsp>CUSTOMIZE</a></li>
			<li><a href=login_logout/about.jsp>ABOUT</a></li>
			<li><a target="iframe1" href=category/production.jsp>PRODUCTION</a></li>
			<li><a target="iframe1" href=category/faq.jsp>FAQ</a></li>
			
			<li><a target="iframe1" href=category/contact.jsp>CONTACT</a></li>

		<%} %>
	</nav>
	<section id="main">

      <iframe name="iframe1" src="category/list_user.jsp" seamless width=100% height=1000px scrolling="no" frameborder="0"> </iframe>
   	</section>


</body>
</html>