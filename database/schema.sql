-- Run this script in SQL Server Management Studio (SSMS) or sqlcmd

IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = N'AC073_VANUR')
BEGIN
    CREATE DATABASE AC073_VANUR;
END
GO

USE AC073_VANUR;
GO

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = N'vanur_records')
BEGIN
    CREATE TABLE vanur_records (
        id              INT IDENTITY(1,1) PRIMARY KEY,
        part_number     NVARCHAR(100)  NOT NULL,
        blo_name        NVARCHAR(200)  NOT NULL,
        blo_designation NVARCHAR(200)  NOT NULL,
        blo_mobile      NVARCHAR(20)   NOT NULL,
        created_at      DATETIME2      NOT NULL DEFAULT GETDATE()
    );
END
GO
