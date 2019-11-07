USE master;  
GO  

--Delete the TestData database if it exists.  
IF EXISTS(SELECT * from sys.databases WHERE name='TestData')  
BEGIN  
    DROP DATABASE TestData;  
END  

--Create a new database called TestData.  
CREATE DATABASE TestTable
   (TestTableID int PRIMARY KEY NOT NULL,  
    Month Date,
	рн nvarchar(
    Price money NULL,  
    ProductDescription text NULL)  
GO

    id = models.ForeignKey
    month = models.DateField()
    to = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    office = models.IntegerField()
    financial_group = models.CharField(max_length=20)
    financial = models.CharField(max_length=20)
    value = models.IntegerField()