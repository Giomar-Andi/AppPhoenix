(function() {
        $("#actualizar").click(function(ev) {
            ev.preventDefault();
            var recol=$('#form-update').serialize();
            const swalWithBootstrapButtons = Swal.mixin({
                customClass: {
                confirmButton: 'btn btn-success',
                cancelButton: 'btn btn-danger'
                },
                buttonsStyling: true
            })
            swalWithBootstrapButtons.fire({
                title: '¿Deseas actualizar los datos de usuario?',
                text: "Recuerda, una vez actualizado los datos,!No hay marcha atras!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Si, actualizar',
                cancelButtonText: 'No, cancelar',
                reverseButtons: true
            }).then((result) => {
                if (result.isConfirmed) {
                    $.ajax({
                        type:'POST',
                        url:'/update_user',
                        data:recol,
                        success:function() {
                            $('#form-update').load('/ajustes.html #form-update');
                            swalWithBootstrapButtons.fire({ 
                                title:'Actualizado',
                                text:'Los datos del usuario se han actualizado correctamente.',
                                icon:'success',
                                showConfirmButton:false,
                                timer:6000,
                                imageUrl: 'https://sm.ign.com/ign_br/screenshot/default/tumblr-o1ezww4zdq1uq80c7o1-500_n3xv.gif',
                                imageWidth: 500,
                                imageHeight: 281,
                                background:'#fff',
                                imageAlt: 'Custom image',
                                showClass:{
                                    popup:'animate__animated animate__fadeInTopLeft'
                                },
                                hideClass:{
                                    popup:'animate__animated animate__fadeOutBottomRight'
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
                    text:'Los datos del usuario se mantienen intactos.',
                    icon:'error',
                    showConfirmButton:false,
                    timer:4000,
                    imageUrl: 'https://truyen2u.net/cover/images/2ceced898a87f59c4bbe29120db089558bacae9c/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f736d514f4f53557a7655627235513d3d2d3234393539333936322e313434393464353063396630663830622e676966',
                    imageWidth: 500,
                    imageHeight: 281,
                    background:'#fff',
                    imageAlt: 'Custom image',
                    showClass:{
                        popup:'animate__animated animate__flip'
                    }
                   })
                }
            })
        })
})();