# APP设计原则

### 商城主要模型
Good
GoodBrand
GoodCategory
GoodImage

Order
DeliverAddress

Coupon
Promotion

Comment
CommentImage
CommentTag

### 主要模块
admin

apps

models

tests

views

### TODOS

- [x] 商品基本模型（name, price)
- [x] 商品CRUD
- [x] 只有创建者才能修改商品，在接口上做这个限制
- [x] 商品列表分页查询+所有字段排序
- [x] 商品分类基本模型 (name)
- [x] 查询商品可以返回对应的分类
- [x] 分类的CRUD
- [x] 查询指定分类下的商品，支持分页和所有字段排序
- [x] 提供一个统计接口的样例，统计不同时间段，如天，小时等，商品创建的数量
