import dearpygui.dearpygui as dpg
import SQL_connection

dpg.create_context()
dpg.create_viewport(title='Python & SQL', width=900, height=500)

# função insert table
with dpg.window(label='insert table', width=300, height=500):
    dpg.add_text("insira os dados na tabela:")

    dpg.add_spacer(height=7)
    dpg.add_input_text(hint='nome', tag='aluno_nome')

    dpg.add_spacer(height=7)
    dpg.add_input_text(hint='sobrenome', tag='aluno_sobrenome')

    dpg.add_spacer(height=7)
    dpg.add_input_text(hint='nota', tag='aluno_nota', decimal=True)

    dpg.add_spacer(height=10)
    dpg.add_button(label='inserir', indent=58, callback=SQL_connection.insert_table)

    dpg.add_spacer(height=10)
    dpg.add_text("", tag='mostra_feedback', indent=10)


# função select table
with dpg.window(label='select table', width=300, height=500, pos=[300]):
    dpg.add_text("verifique os dados da tabela:")

    dpg.add_spacer(height=7)
    dpg.add_input_text(hint='nome', tag='verifica_nome')

    dpg.add_spacer(height=7)
    dpg.add_input_text(hint='sobrenome', tag='verifica_sobrenome')

    dpg.add_spacer(height=7)
    dpg.add_button(label='verificar', indent=62, callback=SQL_connection.select_table)

    dpg.add_spacer(height=8)
    dpg.add_text("", tag='mostra_select_table', indent=10)

# função delete table
with dpg.window(label='delete table', width=300, height=500, pos=[600]):
    dpg.add_text('delete os dados da tabela:')

    dpg.add_spacer(height=7)
    dpg.add_input_text(hint='nome', tag='deleta_nome')

    dpg.add_spacer(height=7)
    dpg.add_input_text(hint='sobrenome', tag='deleta_sobrenome')

    dpg.add_spacer(height=7)
    dpg.add_button(label='deletar', indent=62, callback=SQL_connection.delete_table)

    dpg.add_spacer(height=8)
    dpg.add_text("", tag='deleta_feedback', indent=10)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
