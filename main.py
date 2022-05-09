from Scripts.functions import import_api_exchange_items, answers, less_viewed, new_old_answer, best_rep


def api_stack_exchange_analysis():

    # llamado de funcion para importar datos
    elementos = import_api_exchange_items()

    # 1. Respuestas Contestadas y NO Contestadas
    contestadas, no_contestadas = answers(elementos)
    print('1. Número de respuestas contestadas y no contestadas\n'
          'contestadas: {}\n'
          'no_contestadas: {}\n'.format(contestadas, no_contestadas))

    # 2. Respuestas con menor número de vistas
    id_usuario, vistas, nombre, link_perfil = less_viewed(elementos)
    print('2. Usuario con menor numero de visitas:\n'
          'id_usuario: {} visitas: {} \nnombre: {} link_perfil: {}\n'.format(id_usuario, vistas, nombre,
                                                                             link_perfil))

    # 3. Respuesta más antigua y más actual
    f_reciente, link_actual, f_antigua, link_antigua = new_old_answer(elementos)
    print('3. Respuesta más actual y más antigua:\n'
          'Actual:\n'
          'fecha: {} link: {}\n'
          'Antigua:\n'
          'fecha: {} link: {}\n'.format(f_reciente, link_actual, f_antigua, link_antigua))

    # 4. Respuesta del owner con mayor reputación
    id_usuario, reputacion_max, respuesta = best_rep(elementos)
    print('4. Respuesta del Owner con mayor reputacion: \n'
          'user_id: {}\n'
          'reputación: {}\n'
          'respuesta: {}'.format(id_usuario, reputacion_max, respuesta))


if __name__ == "__main__":
    api_stack_exchange_analysis()
