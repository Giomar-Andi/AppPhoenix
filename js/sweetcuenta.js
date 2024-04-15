(function() {
    $("li div #eliminar").click(function(ev) {
        ev.preventDefault();
        var prop=$(this).parents('li').find('span:first').text();
        var id=$(this).attr('data-id');
        var self=this;
        const swalWithBootstrapButtons = Swal.mixin({
            customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger'
            },
            buttonsStyling: true
        })
        swalWithBootstrapButtons.fire({
            title: '¿Quieres eliminar la cuenta bancaria de '+prop+'?',
            text: "Recuerda, una vez eliminada la cuenta,!No hay marcha atras!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Si, eliminar',
            cancelButtonText: 'No, cancelar',
            reverseButtons: true
        }).then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    type:'POST',
                    url:'/delete_cuenta',
                    data:{'id':id},
                    success:function() {
                        $(self).parents('li').remove();
                        swalWithBootstrapButtons.fire({ 
                            title:'Eliminado',
                            text:'La cuenta bancaria de '+prop+' a sido eliminada correctamente.',
                            icon:'success',
                            showConfirmButton:false,
                            timer:6000,
                            imageUrl: 'https://c.tenor.com/A5CommJKEbwAAAAC/kaneki-ken-tokyo-ghoul.gif',
                            imageWidth: 500,
                            imageHeight: 281,
                            background:'#fff',
                            imageAlt: 'Custom image',
                            showClass:{
                                popup:'animate__animated animate__rotateIn'
                            },
                            hideClass:{
                                popup:'animate__animated animate__rotateOut'
                            },
                        })   
                    }
                });            
            } else if (
                /* Read more about handling dismissals below */
                result.dismiss === Swal.DismissReason.cancel
            ) {
                swalWithBootstrapButtons.fire({ 
                title:'Cancelado',
                text:'La cuenta bancaria de '+prop+' esta intacta.',
                icon:'error',
                showConfirmButton:false,
                timer:4000,
                imageUrl: 'https://i.pinimg.com/originals/f1/de/be/f1debea9b7fc4c701e5881820c2a4bfc.gif',
                imageWidth: 500,
                imageHeight: 281,
                background:'#fff',
                imageAlt: 'Custom image',
                showClass:{
                    popup:'animate__animated animate__zoomInLeft'
                },
                hideClass:{
                    popup:'animate__animated animate__zoomOutRight'
                },
             })
            }
        })
    })
})();