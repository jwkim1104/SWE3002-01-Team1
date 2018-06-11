<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.sql.*" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>회원탈퇴 처리화면</title>
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
	<h2>회원탈퇴 완료</h2>
	<p>
	<hr>
	<p>
<%

	String userId = session.getAttribute("id").toString();
	String sqlList = "DELETE FROM user_ WHERE userID='" + userId + "'";
	stmt.executeUpdate(sqlList);
	
	session.invalidate();
	out.println("회원탈퇴 되었습니다");
	%>
	
	<p><a href=../home.jsp target="xxx">첫 화면</a>으로 돌아가기 </p>
<%	
} catch(SQLException se){
	out.println(se.getMessage());

}
%>
</body>
</html>