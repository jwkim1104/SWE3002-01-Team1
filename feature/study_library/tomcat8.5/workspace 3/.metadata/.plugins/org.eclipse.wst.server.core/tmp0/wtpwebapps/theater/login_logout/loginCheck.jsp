<%@ page language="java" contentType="text/html; charset=UTF-8" import="java.sql.*"
    pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Login Check</title>
<%

Class.forName("com.mysql.jdbc.Driver");
String url="jdbc:mysql://localhost:3306/test_feedbap";
String id="root";
String pw="1234";


try {
	Connection conn = DriverManager.getConnection(url, id, pw);
	Statement stmt = conn.createStatement();
	%>
</head>
<body>
<center>
	<h2>Login Check</h2>
	<p>
	<hr>
	<p>
	<%
	String userId = request.getParameter("id");
	String userPass = request.getParameter("pass");
	String userName = ""; 
	String sqlList = "SELECT userName from user_ where userID='" + userId + "' AND userPW='" + userPass + "'";
	ResultSet rs = stmt.executeQuery(sqlList);
	
	boolean isLogin = false;
	while(rs.next()) {
		//rs.next가 true라면 일치하는 정보가 있다
 	userName = rs.getString(1);

	out.println(userName);
		isLogin = true;
		System.out.print("is done1");
	}
	if(isLogin) {
		System.out.print("is done11");
 		
  		session.setAttribute("name", userName);
		session.setAttribute("id", userId);
		session.setAttribute("pw", userPass);

		System.out.print("is done3");
		
		//response.sendRedirect("../home.jsp");
		request.getRequestDispatcher("../home.jsp").forward(request, response);
		System.out.print(session.getAttribute("name"));

	}
	else {
		%><script> alert("일치하는 회원정보가 없습니다. 아이디와 비밀번호를 확인해 주세요.");
		history.go(-1);
		</script>
		<%
	}

	} catch(SQLException se){
		
		out.println(se.getMessage());
	}
%>
	


</body>
</html>