var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
router.get('/u/:user',function(req,res,next){
	res.send();
})
router.post('/post',function(req,res,next){
	res.send();
})
router.get('/reg',function(req,res,next){
	res.render('reg');
})
router.post('/reg',function(req,res,next){
	res.send();
})
router.get('/login',function(req,res,next){
	res.render('login');
})
router.post('/login',function(req,res,next){
	res.send();
})
router.get('/logout',function(req,res,next){
	res.send();
})

module.exports = router;
