import sqlite3

con = sqlite3.connect("HTitemDB")
cur = con.cursor()

cur.execute("create table itemsTable(pName char(100), pCompany char(50), fPrice char(20), disRate char(10), oriPrice char(50))")
cur.execute("insert into itemsTable values('길단 소프트 무지 반소매 63000', 'GILDAN', '7,900', '68%', '24,900')")
cur.execute("insert into itemsTable values('딥티크 필로시코스 EDP 75ml /딥디크 향수', 'diptyque', '209,800', '20%', '262,250')")
cur.execute("insert into itemsTable values('[소진시 마감] 다용도 방수 핸드폰 거치대', 'THE ERGO', '6,900', '36%', '10,900')")
cur.execute("insert into itemsTable values('철물점 사장님이 개발한 만능 드라이버키트 (98종)', 'BANANABD', '6,900', '53%', '14,900')")
cur.execute("insert into itemsTable values('[4개세트] 굿즈 원형 아이스볼 메이커', 'goods', '7,800', '60%', '19,900')")
cur.execute("insert into itemsTable values('[기코아티크] 피노 무선 충전식 전동 그라인더', 'GIBONGKOREA', '21,900', '86%', '159,000')")
cur.execute("insert into itemsTable values('7321디자인 꾸꾸 태블릿/노트북 파우치-11,13,15인치', '7321 DESIGN', '17,150', '30%', '24,500')")
cur.execute("insert into itemsTable values('컴포지션북 아이패드 케이스', 'COMPOSITION STUDIO', '29,520', '22%', '38,000')")
cur.execute("insert into itemsTable values('모니터 받침대 원목 아크릴 모니터받침대서랍 파티오', 'partyoh', '75,650', '15%', '89,000')")
cur.execute("insert into itemsTable values('한토끼 랜덤팩', 'hanrabbit', '9,610', '19%', '12,000')")
cur.execute("insert into itemsTable values('광동 힘찬하루 男 헛개차 500ml x 20pet', 'KWANGDONG', '17,900', '20%', '22,500')")
cur.execute("insert into itemsTable values('[2kg]춘천 강명희 통다리살 춘천 웰빙 닭갈비', 'ChunCheon Green Food', '23,900', '40%', '40,000')")


con.commit()

# CREATE TABLE `HTitemDB`.`itemsTable` (
#   `pName` VARCHAR(100) NOT NULL,
#   `pCompany` VARCHAR(50) NULL,
#   `fPrice` VARCHAR(20) NULL,
#   `disRate` VARCHAR(10) NULL,
#   `oriPrice` VARCHAR(50) NULL,
#   `itemsImgUrl` VARCHAR(200) NULL,
#   PRIMARY KEY (`pName`));