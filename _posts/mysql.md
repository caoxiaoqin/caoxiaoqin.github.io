---
title: mysql
comments: true
date: 2018-10-15 17:20:11
categories: Mysql
tags: mysql
---

### 数据库 - database - 数据的仓库（集散地）
通过数据库可以实现数据的持久化

当我们做数据持久化操作时，不仅仅是希望能够把数据长久的保存起来，更为重要的是，方便的把需要的数据取出来。

两大类型数据库：

- 关系型数据库 - MySQL
  - 图形化的MySQL客户端工具
    - Navicat for MySQL
- 非关系型数据库 (NoSQL)  
  - Redis - 高速缓存
  - MongoDB - 数据体量大价值低 
  - ElasticSearch - 搜索引擎



1970s IBM - 关系数据库
理论基础：关系代数和集合论
具体表象：用二维表来组织数据

行：记录 - 实体 
列：字段 - 实体的属性

关系型数据库的编程语言：SQL（结构化查询语言）
**SQL由三个部分组成:DDL/DML/DCL**
DDL（数据定义语言）：create / drop / alter
DML（数据操作语言）：insert / delete / update / select
DCL（数据控制语言）：grant(授权) / revoke(召回权限)

关系型数据库产品：Oracle 、 MySQL 、 SQLserver...

- 创建数据库
  `create database <database-name> default charset utf8;`
  (设置默认字符编码)

- 删除数据库
  `drop database if exists <database-name>;`

- 查看数据库
  `show databases;`

- 使用数据库
  `use <database-name>;`

- 查看表格
  `select * from <table-name>;`

####DDL(Data Definition Language)
- 创建二维表
  列名 数据类型 约束条件（非空约束、默认值约束、主键约束）
  主键：表中能够唯一标识一条记录的列
```
create table tb_student
(
stuid int not null, 
stuname varchar(20) not null, 
gender bit not null default 1, 
birth date, 
addr varchar(50),
primary key (stuid)
);
```
补充：not null表示不能为空，varchar(5)-字符串最大为5个字符，char(5)-字符串为5个字符， bit-比特(0，1)， default默认值，primary key-主键

- 删除表
  `drop table if exists <table-name>`
- 清空表
  `truncate table <table-name>;`

- 插入列/删除列
```
alter table tb_student add column tel char(11) not null;
alter table tb_student drop column birth;
```

-  添加唯一性约束
   `alter table tb_college add constraint uni_url unique (url);` 
-  删除索引
   `alter table tb_college drop index uni_url;`

####DML(Data Manipulation Language)

- 插入数据
  `insert into tb_student values (1001, '星辰', 1, '四川', '12345678912');`
  或者
  `insert into tb_student values (1001, '星辰', 1, '四川', '12345232342'),(1002, '李清照', 0, '北京', '12345232342'), (1003, '李白清', 1, '西安', '12345232342');`

- 删除数据
  `delete from tb_student where stuname='星辰';`
  `delete from tb_student where stuid in (1002, 1003);`

- 更新数据
  `update tb_student set addr='四川绵阳', gender=0 where stuid in (1002, 1003);`

- 查询数据
  `select * from tb_student;` -- 查询全表
  `select stuid as 学号, stuname as 姓名 from tb_student;`  -- 别名（alias - as）
  `select stuname as 姓名, if (gender,'boy','girl') as 性别 from tb_student;` -- if中判断条件为mysql专用
  `select stuname as 姓名, case gender when 1 then 'boy' else 'girl' end as 性别 from tb_student;`  -- sql通用
  - 对列做运算
    `select concat(stuname, ':', tel) from tb_student;`  -- 字符串连接

  - 筛选
    `select * from tb_student where stuid between 1002 and 1010;`
    `select * from tb_student where stuid > 1003 and addr is not null;`
    - 模糊查询（vachar、char）
      `select * from tb_student where stuname like '%白%';`  -- %是一个通配符表示零个或者多个任意字符
      `select * from tb_student where stuname like '_白';`  -- _也是一个通配符，表示一个任意字符

      `select * from tb_student where stuname regexp '正则表达式'` -- 正则表达式查询 - regexp - regular expression

    - 排序
      `select * from tb_student order by stuid desc;` -- 降序
      `select * from tb_student order by stuid asc;` -- 升序

    - 分组

      `select if (gender,'男','女') as 性别,count(gender) as 人数 from tb_student group by gender;`

    - 分页
      `select * from tb_student limit 3;`  limit 3-只取前3条记录
      `select * from tb_student limit 3 offset 4;`  offset-跳过
      `select * from tb_student limit 4,3;` 于上一条相同

    - 聚合函数

      `max()/min()/sum()/avg()/count()` - 聚合函数不会把空值纳入计算

  - 子查询 - 在一个查询中用另外一个查询的结果

    `select sname as 姓名,year(now()) - year(birth) as 年龄 from tb_student where birth=(select min(birth) from tb_student);`

  - 连接查询 - 连接多个表进行查询

    `select sname as 姓名, avg(mark) as 平均成绩 from tb_student, tb_score where stuid=sid group by sid;`

  - 左外连接/右外连接

    左外连接- 把左表（写在前面的表）不满足连接条件的记录也查出来对应记录补上null值
    右外连接- 把右表（写在后面的表）不满足连接条件的记录也查出来对应记录补上null值

    `select sname, number from tb_student left join (select sid, count(sid) as number from tb_score group by sid) t1 on t1.sid=tb_student.stuid;`

  注意：去重操作(distinct)和集合运算(in/not in)效率是十分低下的，通常建议用exists或not exists来替代集合运算。
  例如：
  `select ename, job from tbemp where eno in (select distinct mgr from tbemp where mgr is not null);`
  可以用下面的语句等效
  `select ename,job from tbemp t1 where exists (select 'x' from tbemp t2 where t1.eno=t2.mgr);`


#### DCL(Data Control Language)

- 创建用户

`create user 'hellokitty'@'%'identified by '123456';`

- 授权

`grant select on srs.* to 'hellokitty'@'%'; `-- 查看权限
`grant insert,delete,update on srs.* to 'hellokitty'@'%';`   -- 插入，删除，修改表内容的权限
`grant create,drop,alter on srs.* to 'hellokitty'@'%';`  -- 给予创建，删除，修改表的权限
`grant all privileges on srs.* to 'hellokitty'@'%' with grant option;`   -- 授予srs的所有权限,并且可以把自己的权限授予他人。

- 召回

`revoke all privileges on srs.* from 'hellokitty'@'%'; ` -- 召回所有权限

- 事务控制

  当需要一些操作要么全都成功，如果失败一个都不执行的时候使用。

```
begin; -- 开启事务环境
update tb_score set mark=mark-2 where sid=1001 and mark is not null;
update tb_score set mark=mark+2 where sid=1002 and mark is not null;
```

```
commit;  -- 提交(事务才会真正执行)
rollback; -- 事务回滚(失败的时候)
```

- 视图
  视图是查询的快照(把访问权限限制到列上)。
  通过视图可以将用户对表的访问权限进一步加以限制，也就是说将来普通用户不能够直接查询表的数据，只能通过指定的视图去查看到允许他访问的内容。
  - 创建视图

  `create view vw_temp as ...(查询语句);`

  - 查看视图

  `select * from vw_temp;`

- 索引(相当于一本书的目录)

  为表创建索引可以加速查询(用空间换取时间)。

  索引虽然很好，但是不能滥用，一方面索引会浪费空间，另一方面索引会让增删改操作更慢，因为增删改操作调整了数据，所以可能会导致更新索引。

  如果哪个列经常被用于查询的筛选条件，那么这个列就应该建立索引。主键上默认有索引(唯一索引)。

  - 创建索引

    说明：如果使用模糊查询，如果查询条件以%开头，那么索引无效；如果模糊查询的条件不以%开头，则索引有效。

    ```
    create index idx_emp_ename on tbemp(ename); 
    create unique index uni_emp_ename on tbemp(ename);  -- 唯一索引
    ```

  - 删除索引

    `alter teble tbemp drop index idx_emp_ename;`





**数据的完整性**：

- 实体完整性：每一条记录都是独一无二的，没有冗余。 -- 主键/唯一索引(唯一约束)
- 参照完整性：假如B表参照A表，那么A表中没有的记录，B表绝对不能出现。 -- 外键
- 域完整性：录入的数据都是有效的。-- 数据类型 / 非空约束 / 默认值约束 / 检查约束(MySQL中不生效)

#### 表与表之间引用外键：

实体之间关系是可以使用外键

`alter table tb_teacher add column cnum int;`
`alter table tb_teacher add constraint fk_teacher_cnum foreign key (cnum) references tb_college (cnum);`

关系型数据库无法用两张表来表示两个实体之间多对多关系，可以通过添加中间表的方式，在表中添加两个表的外键来实现。



