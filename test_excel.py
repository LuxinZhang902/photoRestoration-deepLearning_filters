import pandas as pd

def export_excel(old_score, dl_score, self_score):
    column = ["Picture {}".format(i + 1) for i in range(16)]
    old_df = pd.DataFrame({'clarity_score': old_score[0],
                           'noise_score': old_score[1],
                           'iso_score': old_score[2],
                           'color_score': old_score[3],
                           'restoration_score': old_score[4]})
    dl_df = pd.DataFrame({'clarity_score': dl_score[0],
                          'noise_score': dl_score[1],
                          'iso_score': dl_score[2],
                          'color_score': dl_score[3],
                          'restoration_score': dl_score[4]})
    self_df = pd.DataFrame({'clarity_score': self_score[0],
                            'noise_score': self_score[1],
                            'iso_score': self_score[2],
                            'color_score': self_score[3],
                            'restoration_score': self_score[4]})
    
    old_df.columns = ['old_' + col for col in old_df.columns]
    dl_df.columns = ['dl_' + col for col in dl_df.columns]
    self_df.columns = ['self_' + col for col in self_df.columns]
    
    combined_df = pd.concat([old_df, dl_df, self_df], axis=1)
    combined_df.insert(0, 'Picture', column)
    combined_df.to_excel('scores.xlsx', index=False)

old_score = [[i*3 for i in range(16)], [i for i in range(16)], [i for i in range(16)], [i for i in range(16)], [i for i in range(16)]]
dl_score = [[i for i in range(16)], [i for i in range(16)], [i for i in range(16)], [i for i in range(16)], [i for i in range(16)]]
self_score = [[i for i in range(16)], [i for i in range(16)], [i for i in range(16)], [i for i in range(16)], [i for i in range(16)]]

export_excel(old_score, dl_score, self_score)