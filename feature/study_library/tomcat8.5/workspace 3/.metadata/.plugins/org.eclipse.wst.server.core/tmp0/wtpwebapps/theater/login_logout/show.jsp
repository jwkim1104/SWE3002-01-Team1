<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>


<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>전체 보기</title>
</head>
<body>
<center><h2>회원 명단</h2></center>

<%

Class.forName("com.mysql.jdbc.Driver");
String url="jdbc:mysql://localhost:3306/test_feedbap";
String id="root";
String pw="1234";


int total = 0;
try {
	Connection conn = DriverManager.getConnection(url, id, pw);
	Statement stmt = conn.createStatement();

	String sqlCount = "SELECT COUNT(*) FROM user_";

	ResultSet rs = stmt.executeQuery(sqlCount);

	if(rs.next()){
		total = rs.getInt(1);
	}

	rs.close();
%>
<center>


<%
if (total == 0) {
%> 등록된 자료가 없습니다. <br>
<% } else { %>
<table width=70%>
	<tr> 
		<th>No</th>
		<th>ID</th>
		<th>이름</th>
		<th>email</th>
		<th>전화번호</th>

	</tr>
	<%
	System.out.println("done");
	String sqlList = "SELECT serialNum, userID, userName, email, phonenumber from user_";
	rs = stmt.executeQuery(sqlList);
	System.out.println("done1");
	while(rs.next()) {
		int serialNum = rs.getInt(1);
		//System.out.println(serialNum);
		String userID = rs.getString(2);
		System.out.println(userID);
		String userName = rs.getString(3);
		System.out.println(userName);
		String email = rs.getString(4);
		System.out.println(email);
		String phonenumber = rs.getString(5);
		System.out.println("done6");
	%>
		
	<tr>
	
		<td><center><%= serialNum %></center></td>
		<td><center><%= userID %></center></td>
		<td><center> <%= userName %> </center></td>
		<td><center><%= email %> </center> </td>
		<td><center><%= phonenumber %></centeR> </td>
	

	</tr>
<%	}
%></table>
<hr>
<p>총 검색 건수 : <%=total %></p>

<%}
} catch(SQLException se) {
	se.printStackTrace();
	out.println("DB Connection Error!");
}
%>



</center>
</body>
</html>