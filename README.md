# dialogue_system_context_recognition
For IBM智慧服务开发大赛

根据项目要求，根据所输入的身份与语句来让后台判断语句所属的类别与所属的对话轮数。针对第一个问题，我提出了一个上文词向量填充的递归模型，根据上文的语句及类别信息来判断当前输入语句所属的类别。对于第二个问题，我暂时没有想到好的办法来区分对话所属的轮数，因为就示例中“如何查看版本？”我认为并没用和之前的问题进行割裂，不属于新的问题。


        dialogue_system_context_recognition/single_dialogue_context_recognition/递归模型.png
      
