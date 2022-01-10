from pycocoevalcap.bleu.bleu import Bleu
from pycocoevalcap.cider.cider import Cider
from pycocoevalcap.meteor.meteor import Meteor
from pycocoevalcap.rouge.rouge import Rouge
from pycocoevalcap.spice.spice import Spice


def _strip(s):
    return s.strip()


def compute_metrics(hypothesis, references, no_overlap=False, no_skipthoughts=False, no_glove=False):
    with open(hypothesis, 'r') as f:
        hyp_list = f.readlines()
    ref_list = []
    for iidx, reference in enumerate(references):
        with open(reference, 'r') as f:
            ref_list.append(f.readlines())
    ref_list = [list(map(_strip, refs)) for refs in zip(*ref_list)]
    refs = {idx: strippedlines for (idx, strippedlines) in enumerate(ref_list)}
    hyps = {idx: [lines.strip()] for (idx, lines) in enumerate(hyp_list)}
    assert len(refs) == len(hyps)

    ret_scores = {}
    if not no_overlap:
        scorers = [
            (Bleu(4), ["Bleu_1", "Bleu_2", "Bleu_3", "Bleu_4"]),
            (Meteor(), "METEOR"),
            (Rouge(), "ROUGE_L"),
            (Cider(), "CIDEr"),
            (Spice(), "SPICE"),
        ]
        for scorer, method in scorers:
            score, scores = scorer.compute_score(refs, hyps)
            if isinstance(method, list):
                for sc, scs, m in zip(score, scores, method):
                    #print("%s: %0.6f" % (m, sc))
                    ret_scores[m] = sc
            else:
                #print("%s: %0.6f" % (method, score))
                ret_scores[method] = score
            # if isinstance(scorer, Meteor):
            #     scorer.close()
        del scorers
    return ret_scores


print(compute_metrics("./Generated Docs/Comment Generation Task/Raw Results/deepcom_5000.trans", ["./Generated Docs/Comment Generation Task/Raw Results/deepcom_5000.ref"]))
print(compute_metrics("./Generated Docs/Comment Generation Task/Raw Results/code2seq_5000.trans", ["./Generated Docs/Comment Generation Task/Raw Results/code2seq_5000.ref"]))
print(compute_metrics("./Generated Docs/Comment Generation Task/Raw Results/re2com_5000.trans", ["./Generated Docs/Comment Generation Task/Raw Results/re2com_5000.ref"]))
print(compute_metrics("./Generated Docs/Commit Message Generation Task/Raw Results/nmt.cleaned.msg.postprocessed", ["./Generated Docs/Commit Message Generation Task/Raw Results/cleaned.test.msg"]))
print(compute_metrics("./Generated Docs/Commit Message Generation Task/Raw Results/nngen.cleaned.test.msg", ["./Generated Docs/Commit Message Generation Task/Raw Results/cleaned.test.msg"]))
print(compute_metrics("./Generated Docs/Commit Message Generation Task/Raw Results/cleaned.test.msg_pointnetwork", ["./Generated Docs/Commit Message Generation Task/Raw Results/cleaned.test.msg"]))
