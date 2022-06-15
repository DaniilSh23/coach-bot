from aiogram.utils.callback_data import CallbackData


callback_training_results_list = CallbackData('@', 'user_tlg_id', 'message_id', 'flag')
callback_for_finish_program = CallbackData('@', 'program_id', 'message_id', 'flag')
callback_for_next_training = CallbackData('@', 'next_training_id', 'message_id', 'flag', 'user_tlg_id')
callback_for_complete_training = CallbackData('@', 'training_id', 'message_id', 'user_tlg_id', 'flag')