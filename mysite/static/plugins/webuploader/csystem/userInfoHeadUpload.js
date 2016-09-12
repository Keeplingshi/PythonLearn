// 图片上传demo
jQuery(function() {
    var $ = jQuery,
    
    	$add_pic = $('#add_pic'),
    	$img=$('#head_img'),
    	
        // 优化retina, 在retina下这个值是2
        ratio = window.devicePixelRatio || 1,

        // 缩略图大小
        thumbnailWidth = 140 * ratio,
        thumbnailHeight = 150 * ratio,

        // Web Uploader实例
        uploader;

    // 初始化Web Uploader
    uploader = WebUploader.create({

        // swf文件路径
        swf: '${pageContext.request.contextPath}/resources/js/webuploader/dist/Uploader.swf',

        // 文件接收服务端。
        server: BASE_URL+'/student/uploaderImg',

        // 选择文件的按钮。可选。
        // 内部根据当前运行是创建，可能是input元素，也可能是flash.
        pick: {
        	id: '#filePicker',
        	multiple: false
        },
        
        //只需上传一个
        fileNumLimit: 1,
        
        //文件大小限制
        fileSingleSizeLimit: 2 * 1024*1024 ,

        // 只允许选择文件，可选。
        accept: {
            title: 'Images',
            extensions: 'gif,jpg,jpeg,bmp,png',
            mimeTypes: 'image/*'
        }
    });
    
    //文件被加入队列前
    uploader.on( 'beforeFileQueued', function( file ) {
    	//如果已有文件，重置队列
    	if(file.size<2 * 1024*1024){
    		uploader.reset();
    	}
    	
    });

    // 当有文件添加进来的时候
    uploader.on( 'fileQueued', function( file ) {
    	//缩略图
        uploader.makeThumb( file, function( error, src ) {
            if ( error ) {
            	$img.replaceWith('<span>不能预览</span>');
                return;
            }

            $img.attr( 'src', src );
        }, thumbnailWidth, thumbnailHeight );
        
    });
    
    uploader.on('error', function(handler) {
    	
		if(handler=="Q_TYPE_DENIED"){
			layer.msg("类型不正确！");
		}
		if(handler=="F_EXCEED_SIZE"){
			layer.msg("请上传2M以下的图片！");
		}
	});

    // 文件上传过程中创建进度条实时显示。
    uploader.on( 'uploadProgress', function( file, percentage ) {
        
    });

    // 文件上传成功，给item添加成功class, 用样式标记上传成功。
    uploader.on( 'uploadSuccess', function( file, data ) {
    	layer.msg("上传成功");
    	$("#headImg").val(data._raw);
    	
		var form = $("#studentFormId");
		form.ajaxSubmit(function(result){
			if(result=='success'){

				parent.layer.msg('成功', {
					offset: ['260px'],
     		        time: 1500//1.5s后自动关闭
     		    });
				//关闭当前新增页面页
				var index = parent.layer.getFrameIndex(window.name); //先得到当前iframe层的索引
				parent.layer.close(index); //再执行关闭    
			}else{
				layer.msg('新增失败',{
					offset: ['260px']
				});
			}
		});
    });

    // 文件上传失败，现实上传出错。
    uploader.on( 'uploadError', function( file ) {
    	layer.msg("上传出错");
    });

    // 完成上传完了，成功或者失败，先删除进度条。
    uploader.on( 'uploadComplete', function( file ) {
    });
    
    
   $("#saveButton").click(function(){

		var stuIdVal=$("#stuId").val();		//学号
		var stunameVal=$("#stuname").val();	//姓名
		var classIdVal=$("#classId").val();	//班级
		
		if(stuIdVal==null||stuIdVal==''){
			layer.tips('学号不能为空', '#stuId');
			return;
		}

		if(stunameVal==null||stunameVal==''){
			layer.tips('姓名不能为空', '#stuname');
			return;
		}
		
		if(classIdVal==null||classIdVal==''){
			layer.tips('班级不能为空', '#class_select_add_id');
			return;
		}
		
		//如果有文件，则上传，成功后
		if(uploader.getFiles()[0]!=null){
		   	uploader.options.formData={stuId:stuIdVal}; 
	    	uploader.upload();
	    	return;
		}
		
		var form = $("#studentFormId");
		form.ajaxSubmit(function(result){
			if(result=='success'){

				parent.layer.msg('成功', {
					offset: ['260px'],
     		        time: 1500//1.5s后自动关闭
     		    });
				//关闭当前新增页面页
				var index = parent.layer.getFrameIndex(window.name); //先得到当前iframe层的索引
				parent.layer.close(index); //再执行关闭    
			}else{
				layer.msg('失败',{
					offset: ['260px']
				});
			}
		});
    	
    });
});