from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .models import UserOwner, Category, Compress
from Users.models import Users


def orderb(id):

    # this order is point

    # if id == 6:
    #     order = 5000

    # else:
    order = 2000000

    return order


def order_list(id):

    # this order list is the list of every order seprated and is rial

    list = [id, 2, 3]

    return list


def get_user_owner(request):

    code = request.GET.get('code')

    if request.user.is_authenticated:
        userId = request.user.id
        ownerId = Users.objects.filter(identifierـcode=code).first().id

        if ownerId is not None:
            owner_user = UserOwner.objects.create(MlmOwner_id=ownerId, MlmUser_id=userId)

    return HttpResponse('...')


def branches(id):

    owner = Users.objects.filter(id=id).first()
    mlmuser = []

    if owner is None:
        return HttpResponse('there is no user whit this code')

    else:
        branches = UserOwner.objects.filter(MlmOwner_id=id).all()
        branches_no = UserOwner.objects.filter(MlmOwner_id=id).all().count()

        if branches is not None:
            for i in range(branches_no):
                mlmuser.append(branches[i].MlmUser)
        else:
            mlmuser = None


    return mlmuser


def Order(id):

    # this order is point in pdf

    sum_order = orderb(id)
    if branches(id) is not None:
        for br1 in branches(id):
            sum_order += orderb(br1.id)
            if branches(br1.id) is not None:
                for br2 in branches(br1.id):
                    sum_order += orderb(br2.id)
                    if branches(br2.id) is not None:
                        for br3 in branches(br2.id):
                            sum_order += orderb(br3.id)
                            if branches(br3.id) is not None:
                                for br4 in branches(br3.id):
                                    sum_order += orderb(br4.id)
                                    if branches(br4.id) is not None:
                                        for br5 in branches(br4.id):
                                            sum_order += orderb(br5.id)
                                            if branches(br5.id) is not None:
                                                for br6 in branches(br5.id):
                                                    sum_order += orderb(br6.id)
                                                    if branches(br6.id) is not None:
                                                        for br7 in branches(br6.id):
                                                            sum_order += orderb(br7.id)

    return sum_order


def Stars(category, Id):

    list = []
    listC = {}
    gp_category = []
    stars = 0


    if branches(Id) is not None:
        for i in branches(Id):
            order = orderb(i.id)
            cate = Category.objects.filter(Id_id=i.id).first()
            if cate is not None:
                cate = cate.OwnerCategory
                listC[cate] = orderb(i.id)

            list.append(order)
            gp_category.append(cate)


    cat_uptala = ['tala', 'morvarid', 'yaghoot', 'zomorod', 'almas', 'almas_abi', 'almas_sorkh', 'almas_siah', 'safir_tala', 'safir_morvarid', 'safir_yaghoot', 'safir_zomorod', 'safir_almas', 'safir_almas_abi', 'safir_almas_sorkh']
    cat_upmorvarid = cat_uptala[1:]
    cat_upyaghoot = cat_upmorvarid[1:]
    cat_upzomorod = cat_upyaghoot[1:]
    cat_upalmas = cat_upzomorod[1:]
    cat_upalmas_abi = cat_upalmas[1:]
    cat_upalmas_sorkh = cat_upalmas_abi[1:]
    cat_upalmas_siah = cat_upalmas_sorkh[1:]
    cat_upsafir_tala = cat_upalmas_siah[1:]
    cat_upsafir_morvarid = cat_upsafir_tala[1:]
    cat_upsafir_yaghoot = cat_upsafir_morvarid[1:]
    cat_upsafir_zomorod = cat_upsafir_yaghoot[1:]
    cat_upsafir_almas = cat_upsafir_zomorod[1:]
    cat_upsafir_almas_abi = cat_upsafir_almas[1:]
    print(gp_category)
    print(category)
    print(list)
    if category == 'bronze':

        j = 0

        for i in list:

            if len(list) != 0:
                userOrder = max(list)
                list.remove(userOrder)
            else:
                userOrder = 0

            if j == 0:
                for k in range(len(list) + 1):
                    if userOrder >= 50:
                        j += 1
                        break

                    else:
                        userOrder += min(list)
                        list.remove(min(list))

            if j == 1:
                for k in range(len(list) + 1):
                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break
                    if userOrder >= 50:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)
                            if userOrder >= 50:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


        stars = j


    if category == 'noghre':

        j = 0

        for i in list:

            if len(list) != 0:
                userOrder = max(list)
                list.remove(userOrder)
            else:
                userOrder = 0

            if j == 0:
                for k in range(len(list)+1):

                    if userOrder >= 1000:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                        else:
                            break


            if j == 1:
                for k in range(len(list)+1):
                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break
                    if userOrder >= 500:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)
                            if userOrder >= 500:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break



        stars = j


    if category == 'tala':

            j = 0

            for i in list:

                if len(list) != 0:
                    userOrder = max(list)
                    list.remove(userOrder)

                if j == 0:
                    for k in range(len(list) + 1):

                        if userOrder >= 2000:
                            j += 1
                            break


                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))

                            else:
                                break


                if j == 1:
                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break
                        if userOrder >= 1000:
                            j += 1
                            break

                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)
                                if userOrder >= 1000:
                                    list.remove(userOrder)
                                    j += 1
                                    break
                            else:
                                break

                if j == 2:
                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break
                        if userOrder >= 50:
                            j += 1
                            break

                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)
                                if userOrder >= 50:
                                    list.remove(userOrder)
                                    j += 1
                                    break
                            else:
                                break



            stars = j


    if category == 'morvarid':

        j = 0
        for c in gp_category:
            if c in cat_uptala:
                list.remove(listC[c])
                j += 1
                break

        for i in list:

            if len(list) != 0:
                userOrder = max(list)
                list.remove(userOrder)

            if j == 1:
                for k in range(len(list) + 1):

                    if userOrder >= 2000:
                        j += 1
                        break


                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))

                            if userOrder >= 2000:
                                j += 1
                                break
                        else:
                            break


            if j == 2:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break
                    if userOrder >= 500:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 500:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break

        stars = j


    if category == 'yaghoot':

        j = 0
        for c1 in gp_category:
            if c1 in cat_upmorvarid:
                j += 1
                gp_category.remove(c1)
                list.remove(listC[c1])
                break

        for c2 in gp_category:
            if c2 in cat_uptala:
                j += 1
                gp_category.remove(c2)
                list.remove(listC[c2])
                break

        for i in list:

            if len(list) != 0:

                userOrder = max(list)
                list.remove(userOrder)

            if j == 2:
                for k in range(len(list) + 1):

                    if userOrder >= 1000:
                        j += 1
                        break


                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))

                            if userOrder >= 1000:
                                j += 1
                                break
                        else:
                            break


            if j == 3:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)

                    else:
                        break

                    if userOrder >= 500:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 500:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


            if j == 4:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 250:
                        j += 1
                        break
                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 250:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


            if j >= 5:
                for m in range(len(list)):
                    if len(list) == 0:
                        break

                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break

                        if userOrder >= 125:
                            j += 1
                            break
                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)

                                if userOrder >= 125:
                                    j += 1
                                    list.remove(userOrder)
                                    break
                            else:
                                break

        stars = j


    if category == 'zomorod':

        j = 0
        for c1 in gp_category:
            if c1 in cat_upyaghoot:
                j += 1
                gp_category.remove(c1)
                list.remove(listC[c1])
                break

        for c2 in gp_category:
            if c2 in cat_upmorvarid:
                j += 1
                gp_category.remove(c2)
                list.remove(listC[c2])
                break

        for i in list:

            if len(list) != 0:

                userOrder = max(list)
                list.remove(userOrder)

            if j == 2:
                for k in range(len(list) + 1):

                    if userOrder >= 2000:
                        j += 1
                        break


                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))

                            if userOrder >= 2000:
                                j += 1
                                break
                        else:
                            break


            if j == 3:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 1000:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 1000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


            if j == 4:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 500:
                        j += 1
                        break
                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 500:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break

            if j >= 5:
                for m in range(len(list)):
                    if len(list) == 0:
                        break

                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break

                        if userOrder >= 250:
                            j += 1
                            break
                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)

                                if userOrder >= 250:
                                    j += 1
                                    list.remove(userOrder)
                                    break
                            else:
                                break

        stars = j


    if category == 'almas':

        j = 0
        for c1 in gp_category:
            if c1 in cat_upzomorod:
                j += 1
                gp_category.remove(c1)
                list.remove(listC[c1])
                break

        for c2 in gp_category:
            if c2 in cat_upyaghoot:
                j += 1
                gp_category.remove(c2)
                list.remove(listC[c2])
                break

        for i in list:

            if len(list) != 0:

                userOrder = max(list)
                list.remove(userOrder)

            if j == 2:
                for k in range(len(list) + 1):

                    if userOrder >= 6000:
                        j += 1
                        break


                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))

                            if userOrder >= 6000:
                                j += 1
                                break
                        else:
                            break


            if j == 3:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 3000:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 3000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


            if j == 4:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 1500:
                        j += 1
                        break
                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 1500:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break

            if j >= 5:
                for m in range(len(list)):
                    if len(list) == 0:
                        break

                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break

                        if userOrder >= 750:
                            j += 1
                            break
                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)

                                if userOrder >= 750:
                                    j += 1
                                    list.remove(userOrder)
                                    break
                            else:
                                break

        stars = j


    if category == 'almas_abi':

        j = 0
        for c1 in gp_category:
            if c1 in cat_upalmas:
                j += 1
                gp_category.remove(c1)
                list.remove(listC[c1])
                break

        for c2 in gp_category:
            if c2 in cat_upzomorod:
                j += 1
                gp_category.remove(c2)
                list.remove(listC[c2])
                break

        for i in list:

            if len(list) != 0:

                userOrder = max(list)
                list.remove(userOrder)

            if j == 2:
                for k in range(len(list) + 1):

                    if userOrder >= 18000:
                        j += 1
                        break


                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))

                            if userOrder >= 18000:
                                j += 1
                                break
                        else:
                            break


            if j == 3:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 9000:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 9000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


            if j == 4:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 4500:
                        j += 1
                        break
                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 4500:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break

            if j >= 5:
                for m in range(len(list)):
                    if len(list) == 0:
                        break

                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break

                        if userOrder >= 2000:
                            j += 1
                            break
                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)

                                if userOrder >= 2000:
                                    j += 1
                                    list.remove(userOrder)
                                    break
                            else:
                                break

        stars = j


    if category == 'almas_siah':

        j = 0
        for c1 in gp_category:
            if c1 in cat_upalmas_sorkh:
                j += 1
                gp_category.remove(c1)
                list.remove(listC[c1])
                break

        for c2 in gp_category:
            if c2 in cat_upalmas_abi:
                j += 1
                gp_category.remove(c2)
                list.remove(listC[c2])
                break

        for i in list:

            if len(list) != 0:

                userOrder = max(list)
                list.remove(userOrder)

            if j == 2:
                for k in range(len(list) + 1):

                    if userOrder >= 150000:
                        j += 1
                        break


                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))

                            if userOrder >= 150000:
                                j += 1
                                break
                        else:
                            break


            if j == 3:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 75000:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 75000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


            if j == 4:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 38000:
                        j += 1
                        break
                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 38000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break

            if j >= 5:
                for m in range(len(list)):
                    if len(list) == 0:
                        break

                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break

                        if userOrder >= 18000:
                            j += 1
                            break
                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)

                                if userOrder >= 18000:
                                    j += 1
                                    list.remove(userOrder)
                                    break
                            else:
                                break

        stars = j


    if category == 'safir_tala':

        j = 0
        for c1 in gp_category:
            if c1 in cat_upalmas_siah:
                j += 1
                gp_category.remove(c1)
                list.remove(listC[c1])
                break

        for c2 in gp_category:
            if c2 in cat_upalmas_sorkh:
                j += 1
                gp_category.remove(c2)
                list.remove(listC[c2])
                break

        for i in list:

            if len(list) != 0:

                userOrder = max(list)
                list.remove(userOrder)

            if j == 2:
                for k in range(len(list) + 1):

                    if userOrder >= 450000:
                        j += 1
                        break


                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))

                            if userOrder >= 450000:
                                j += 1
                                break
                        else:
                            break


            if j == 3:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 225000:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 225000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


            if j == 4:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 112000:
                        j += 1
                        break
                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 112000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break

            if j >= 5:
                for m in range(len(list)):
                    if len(list) == 0:
                        break

                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break

                        if userOrder >= 54000:
                            j += 1
                            break
                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)

                                if userOrder >= 54000:
                                    j += 1
                                    list.remove(userOrder)
                                    break
                            else:
                                break

        stars = j


    if category == 'safir_morvarid':

        j = 0
        for c1 in gp_category:
            if c1 in cat_upsafir_tala:
                j += 1
                gp_category.remove(c1)
                list.remove(listC[c1])
                break

        for c2 in gp_category:
            if c2 in cat_upalmas_siah:
                j += 1
                gp_category.remove(c2)
                list.remove(listC[c2])
                break

        for i in list:

            if len(list) != 0:

                userOrder = max(list)
                list.remove(userOrder)

            if j == 2:
                for k in range(len(list) + 1):

                    if userOrder >= 1300000:
                        j += 1
                        break


                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))

                            if userOrder >= 1300000:
                                j += 1
                                break
                        else:
                            break


            if j == 3:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 650000:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 650000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


            if j == 4:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 325000:
                        j += 1
                        break
                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 325000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break

            if j >= 5:
                for m in range(len(list)):
                    if len(list) == 0:
                        break

                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break

                        if userOrder >= 160000:
                            j += 1
                            break
                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)

                                if userOrder >= 160000:
                                    j += 1
                                    list.remove(userOrder)
                                    break
                            else:
                                break

        stars = j


    if category == 'safir_yaghoot':

        j = 0
        for c1 in gp_category:
            if c1 in cat_upsafir_morvarid:
                j += 1
                gp_category.remove(c1)
                list.remove(listC[c1])
                break

        for c2 in gp_category:
            if c2 in cat_upsafir_tala:
                j += 1
                gp_category.remove(c2)
                list.remove(listC[c2])
                break

        for i in list:

            if len(list) != 0:

                userOrder = max(list)
                list.remove(userOrder)

            if j == 2:
                for k in range(len(list) + 1):

                    if userOrder >= 4500000:
                        j += 1
                        break


                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))

                            if userOrder >= 4500000:
                                j += 1
                                break
                        else:
                            break


            if j == 3:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 2250000:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 2250000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


            if j == 4:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 1125000:
                        j += 1
                        break
                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 1125000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break

            if j >= 5:
                for m in range(len(list)):
                    if len(list) == 0:
                        break

                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break

                        if userOrder >= 480000:
                            j += 1
                            break
                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)

                                if userOrder >= 480000:
                                    j += 1
                                    list.remove(userOrder)
                                    break
                            else:
                                break

        stars = j


    if category == 'safir_zomorod':

        j = 0
        for c1 in gp_category:
            if c1 in cat_upsafir_yaghoot:
                j += 1
                gp_category.remove(c1)
                list.remove(listC[c1])
                break

        for c2 in gp_category:
            if c2 in cat_upsafir_morvarid:
                j += 1
                gp_category.remove(c2)
                list.remove(listC[c2])
                break

        for i in list:

            if len(list) != 0:

                userOrder = max(list)
                list.remove(userOrder)

            if j == 2:
                for k in range(len(list) + 1):

                    if userOrder >= 13000000:
                        j += 1
                        break


                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))

                            if userOrder >= 13000000:
                                j += 1
                                break
                        else:
                            break


            if j == 3:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 6500000:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 6500000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


            if j == 4:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 3250000:
                        j += 1
                        break
                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 3250000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break

            if j >= 5:
                for m in range(len(list)):
                    if len(list) == 0:
                        break

                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break

                        if userOrder >= 1500000:
                            j += 1
                            break
                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)

                                if userOrder >= 1500000:
                                    j += 1
                                    list.remove(userOrder)
                                    break
                            else:
                                break

        stars = j


    if category == 'safir_almas':

        j = 0
        for c1 in gp_category:
            if c1 in cat_upsafir_zomorod:
                j += 1
                gp_category.remove(c1)
                list.remove(listC[c1])
                break

        for c2 in gp_category:
            if c2 in cat_upsafir_yaghoot:
                j += 1
                gp_category.remove(c2)
                list.remove(listC[c2])
                break

        for i in list:

            if len(list) != 0:

                userOrder = max(list)
                list.remove(userOrder)

            if j == 2:
                for k in range(len(list) + 1):

                    if userOrder >= 39000000:
                        j += 1
                        break


                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))

                            if userOrder >= 39000000:
                                j += 1
                                break
                        else:
                            break


            if j == 3:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 19500000:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 19500000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


            if j == 4:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 9750000:
                        j += 1
                        break
                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 9750000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break

            if j >= 5:
                for m in range(len(list)):
                    if len(list) == 0:
                        break

                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break

                        if userOrder >= 4875000:
                            j += 1
                            break
                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)

                                if userOrder >= 4875000:
                                    j += 1
                                    list.remove(userOrder)
                                    break
                            else:
                                break

        stars = j


    if category == 'safir_almas_abi':

        j = 0
        for c1 in gp_category:
            if c1 in cat_upsafir_almas:
                j += 1
                gp_category.remove(c1)
                list.remove(listC[c1])
                break

        for c2 in gp_category:
            if c2 in cat_upsafir_zomorod:
                j += 1
                gp_category.remove(c2)
                list.remove(listC[c2])
                break

        for i in list:

            if len(list) != 0:

                userOrder = max(list)
                list.remove(userOrder)

            if j == 2:
                for k in range(len(list) + 1):

                    if userOrder >= 117000000:
                        j += 1
                        break


                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))

                            if userOrder >= 117000000:
                                j += 1
                                break
                        else:
                            break


            if j == 3:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 58500000:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 58500000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


            if j == 4:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 29250000:
                        j += 1
                        break
                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 29250000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break

            if j >= 5:
                for m in range(len(list)):
                    if len(list) == 0:
                        break

                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break

                        if userOrder >= 14625000:
                            j += 1
                            break
                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)

                                if userOrder >= 14625000:
                                    j += 1
                                    list.remove(userOrder)
                                    break
                            else:
                                break

        stars = j


    if category == 'safir_almas_sorkh':

        j = 0
        for c1 in gp_category:
            if c1 in cat_upsafir_almas_abi:
                j += 1
                gp_category.remove(c1)
                list.remove(listC[c1])
                break

        for c2 in gp_category:
            if c2 in cat_upsafir_almas:
                j += 1
                gp_category.remove(c2)
                list.remove(listC[c2])
                break

        for i in list:

            if len(list) != 0:

                userOrder = max(list)
                list.remove(userOrder)

            if j == 2:
                for k in range(len(list) + 1):

                    if userOrder >= 351000000:
                        j += 1
                        break


                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))

                            if userOrder >= 351000000:
                                j += 1
                                break
                        else:
                            break


            if j == 3:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 175500000:
                        j += 1
                        break

                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 175500000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break


            if j == 4:

                for k in range(len(list) + 1):

                    if len(list) != 0:
                        userOrder = max(list)
                        list.remove(userOrder)
                    else:
                        break

                    if userOrder >= 87750000:
                        j += 1
                        break
                    else:
                        if len(list) != 0:
                            userOrder += min(list)
                            list.remove(min(list))
                            list.append(userOrder)

                            if userOrder >= 87750000:
                                list.remove(userOrder)
                                j += 1
                                break
                        else:
                            break

            if j >= 5:
                for m in range(len(list)):
                    if len(list) == 0:
                        break

                    for k in range(len(list) + 1):
                        if len(list) != 0:
                            userOrder = max(list)
                            list.remove(userOrder)
                        else:
                            break

                        if userOrder >= 43875000:
                            j += 1
                            break
                        else:
                            if len(list) != 0:
                                userOrder += min(list)
                                list.remove(min(list))
                                list.append(userOrder)

                                if userOrder >= 43875000:
                                    j += 1
                                    list.remove(userOrder)
                                    break
                            else:
                                break

        stars = j

    return stars


def category(request):

    if request.user.is_authenticated:
        Id = request.user.id

    else:
        return HttpResponse('first login')

    categoryN(Id)

    return categoryN(Id)


def categoryN(id):


    Id = id
    order = Order(Id)
    order_s1 = []
    cat_s1 = []


    if branches(Id) is not None:
        for br1 in branches(Id):

            order1 = orderb(br1.id)
            order_s1.append(order1)
            cate = Category.objects.filter(Id_id=br1.id).order_by('-id').first()

            if cate is not None:
                cat_s1.append(cate.OwnerCategory)

            else:

                categoryN(br1.id)


            order1 = orderb(br1.id)
            order_s1.append(order1)
            cate = Category.objects.filter(Id_id=br1.id).order_by('-id').first()

            if cate is not None:
                cat_s1.append(cate.OwnerCategory)





    j = 0
    flag = 0
    cat_uptala = ['tala', 'morvarid', 'yaghoot', 'zomorod', 'almas', 'almas_abi', 'almas_sorkh', 'almas_siah',
                  'safir_tala', 'safir_morvarid', 'safir_yaghoot', 'safir_zomorod', 'safir_almas', 'safir_almas_abi',
                  'safir_almas_sorkh']
    cat_upmorvarid = cat_uptala[1:]
    cat_upyaghoot = cat_upmorvarid[1:]
    cat_upzomorod = cat_upyaghoot[1:]
    cat_upalmas = cat_upzomorod[1:]
    cat_upalmas_abi = cat_upalmas[1:]
    cat_upalmas_sorkh = cat_upalmas_abi[1:]
    cat_upalmas_siah = cat_upalmas_sorkh[1:]
    cat_upsafir_tala = cat_upalmas_siah[1:]
    cat_upsafir_morvarid = cat_upsafir_tala[1:]
    cat_upsafir_yaghoot = cat_upsafir_morvarid[1:]
    cat_upsafir_zomorod = cat_upsafir_yaghoot[1:]
    cat_upsafir_almas = cat_upsafir_zomorod[1:]
    cat_upsafir_almas_abi = cat_upsafir_almas[1:]


    if order >= 27000000000:
        if cat_s1:
            for i in cat_s1:
                if i in cat_upsafir_almas_abi:
                    j += 1
                    cat_s1.remove(i)

            if j >= 1:
                j = 1
                for i in cat_s1:
                    if i in cat_upsafir_almas:
                        j += 1
                        cat_s1.remove(i)

                if j >= 2:
                    j = 2
                    for i in order_s1:
                        if i >= 351000000:
                            j += 1

                        else:
                            flag = 1

                    if j >= 3 and flag != 1:
                        Category.objects.create(OwnerCategory='safir_almas_sorkh', stars=Stars('safir_almas_sorkh', Id), Id_id=Id)
                        return HttpResponse('your group is safir_almas_sorkh')

    if j < 3:
        j = 0
        if order >= 9000000000:
            if cat_s1:
                for i in cat_s1:
                    if i in cat_upsafir_almas:
                        j += 1
                        cat_s1.remove(i)

                if j >= 1:
                    j = 1
                    for i in cat_s1:
                        if i in cat_upsafir_zomorod:
                            j += 1
                            cat_s1.remove(i)

                    if j >= 2:
                        j = 2
                        for i in order_s1:
                            if i >= 117000000:
                                j += 1

                            else:
                                flag = 1

                        if j >= 3 and flag != 1:
                            Category.objects.create(OwnerCategory='safir_almas_abi', stars=Stars('safir_almas_abi', Id), Id_id=Id)
                            return HttpResponse('your group is safir_almas_abi')

    if j < 3:
        j = 0
        if order >= 3000000000:
            if cat_s1:
                for i in cat_s1:
                    if i in cat_upsafir_zomorod:
                        j += 1
                        cat_s1.remove(i)

                if j >= 1:
                    j = 1
                    for i in cat_s1:
                        if i in cat_upsafir_yaghoot:
                            j += 1
                            cat_s1.remove(i)

                    if j >= 2:
                        j = 2
                        for i in order_s1:
                            if i >= 39000000:
                                j += 1

                            else:
                                flag = 1

                        if j >= 3 and flag != 1:
                            Category.objects.create(OwnerCategory='safir_almas', stars=Stars('safir_almas', Id), Id_id=Id)
                            return HttpResponse('your group is safir_almas')

    if j < 3:
        j = 0
        if order >= 1000000000:
            if cat_s1:
                for i in cat_s1:
                    if i in cat_upsafir_zomorod:
                        j += 1
                        cat_s1.remove(i)

                if j >= 1:
                    j = 1
                    for i in cat_s1:
                        if i in cat_upsafir_yaghoot:
                            j += 1
                            cat_s1.remove(i)

                    if j >= 2:
                        j = 2
                        for i in order_s1:
                            if i >= 13000000:
                                j += 1

                            else:
                                flag = 1

                        if j >= 3 and flag != 1:
                            Category.objects.create(OwnerCategory='safir_zomorod', stars=Stars('safir_zomorod', Id), Id_id=Id)
                            return HttpResponse('your group is safir_zomorod')

    if j < 3:
        j = 0
        if order >= 330000000:
            if cat_s1:
                for i in cat_s1:
                    if i in cat_upsafir_yaghoot:
                        j += 1
                        cat_s1.remove(i)

                if j >= 1:
                    j = 1
                    for i in cat_s1:
                        if i in cat_upsafir_morvarid:
                            j += 1
                            cat_s1.remove(i)

                    if j >= 2:
                        j = 2
                        for i in order_s1:
                            if i >= 4500000:
                                j += 1

                            else:
                                flag = 1

                        if j >= 3 and flag != 1:
                            Category.objects.create(OwnerCategory='safir_yaghoot', stars=Stars('safir_yaghoot', Id), Id_id=Id)
                            return HttpResponse('your group is safir_yaghoot')

    if j < 3:
        j = 0
        if order >= 110000000:
            if cat_s1:
                for i in cat_s1:
                    if i in cat_upsafir_tala:
                        j += 1
                        cat_s1.remove(i)
                        if j == 1:
                            break

                if j == 1:
                    for i in cat_s1:
                        if i in cat_upalmas_siah:
                            j += 1
                            cat_s1.remove(i)
                            if j == 2:
                                break

                    if j == 2:
                        for i in order_s1:
                            if i >= 1300000:
                                j += 1

                            else:
                                flag = 1

                        if j >= 3 and flag != 1:
                            Category.objects.create(OwnerCategory='safir_morvarid', stars=Stars('safir_morvarid', Id), Id_id=Id)
                            return HttpResponse('your group is safir_morvarid')

    if j < 3:
        j = 0
        if order >= 36000000:
            if cat_s1:
                for i in cat_s1:
                    if i in cat_upalmas_siah:
                        j += 1
                        cat_s1.remove(i)
                        if j == 1:
                            break

                if j == 1:
                    for i in cat_s1:
                        if i in cat_upalmas_sorkh:
                            j += 1
                            cat_s1.remove(i)
                            if j == 2:
                                break

                    if j == 2:
                        for i in order_s1:
                            if i >= 450000:
                                j += 1

                            else:
                                flag = 1

                        if j >= 3 and flag != 1:
                            Category.objects.create(OwnerCategory='safir_tala', stars=Stars('safir_tala', Id), Id_id=Id)
                            return HttpResponse('your group is safir_tala')

    if j < 3:
        if order >= 12000000:
            if cat_s1:
                for i in cat_s1:
                    if i in cat_upalmas_sorkh:
                        j += 1
                        cat_s1.remove(i)
                        if j == 1:
                            break

                if j == 1:
                    for i in cat_s1:
                        if i in cat_upalmas_abi:
                            j += 1
                            cat_s1.remove(i)
                            if j == 2:
                                break

                    if j == 2:
                        for i in order_s1:
                            if i >= 150000:
                                j += 1

                            else:
                                flag = 1

                        if j >= 3 and flag != 1:
                            Category.objects.create(OwnerCategory='almas_siah', stars=Stars('almas_siah', Id), Id_id=Id)
                            return HttpResponse('your group is almas_siah')

    if j < 3:
        if order >= 4000000:
            if cat_s1:
                for i in cat_s1:
                    if i in cat_upalmas_abi:
                        j += 1
                        cat_s1.remove(i)
                        if j == 1:
                            break

                if j == 1:
                    for i in cat_s1:
                        if i in cat_upalmas:
                            j += 1
                            cat_s1.remove(i)
                            if j == 2:
                                break

                    if j == 2:
                        for i in order_s1:
                            if i >= 50000:
                                j += 1

                            else:
                                flag = 1

                        if j >= 3 and flag != 1:
                            Category.objects.create(OwnerCategory='almas_sorkh', stars=Stars('almas_sorkh', Id), Id_id=Id)
                            return HttpResponse('your group is almas_sorkh')

    if j < 3:
        if order >= 1200000:
            if cat_s1:
                for i in cat_s1:
                    if i in cat_upalmas:
                        j += 1
                        cat_s1.remove(i)
                        if j == 1:
                            break

                if j == 1:
                    for i in cat_s1:
                        if i in cat_upzomorod:
                            j += 1
                            cat_s1.remove(i)
                            if j == 2:
                                break

                    if j == 2:
                        for i in order_s1:
                            if i >= 18000:
                                j += 1

                            else:
                                flag = 1

                        if j >= 3 and flag != 1:
                            Category.objects.create(OwnerCategory='almas_abi', stars=Stars('almas_abi', Id), Id_id=Id)
                            return HttpResponse('your group is almas_abi')

    if j < 3:
        if order >= 320000:
            if cat_s1:
                for i in cat_s1:
                    if i in cat_upzomorod:
                        j += 1
                        cat_s1.remove(i)
                        if j == 1:
                            break

                if j == 1:
                    for i in cat_s1:
                        if i in cat_upyaghoot:
                            j += 1
                            cat_s1.remove(i)
                            if j == 2:
                                break

                    if j == 2:
                        for i in order_s1:
                            if i >= 6000:
                                j += 1

                            else:
                                flag = 1

                        if j >= 3 and flag != 1:
                            Category.objects.create(OwnerCategory='almas', stars=Stars('almas', Id), Id_id=Id)
                            return HttpResponse('your group is almas')

    if j < 3:
        if order >= 90000:
            if cat_s1:
                for i in cat_s1:
                    if i in cat_upyaghoot:
                        j += 1
                        cat_s1.remove(i)
                        if j == 1:
                            break

                if j == 1:
                    for i in cat_s1:
                        if i in cat_upmorvarid:
                            j += 1
                            cat_s1.remove(i)
                            if j == 2:
                                break

                    if j == 2:
                        for i in order_s1:
                            if i >= 2000:
                                j += 1

                            else:
                                flag = 1

                        if j >= 3 and flag != 1:
                            Category.objects.create(OwnerCategory='zomorod', stars=Stars('zomorod', Id), Id_id=Id)
                            return HttpResponse('your group is zomorod')

    if j < 3:
        if order >= 33000:
            if cat_s1:
                for i in cat_s1:
                    if i in cat_upmorvarid:
                        j += 1
                        cat_s1.remove(i)
                        if j == 1:
                            break

                if j == 1:
                    for i in cat_s1:
                        if i in cat_uptala:
                            j += 1
                            cat_s1.remove(i)
                            if j == 2:
                                break

                    if j == 2:
                        for i in order_s1:
                            if i >= 1000:
                                j += 1

                            else:
                                flag = 1

                        if j >= 3 and flag != 1:
                            Category.objects.create(OwnerCategory='yaghoot', stars=Stars('yaghoot', Id), Id_id=Id)
                            return HttpResponse('your group is yaghoot')

    if j < 3:
        j = 0
        if order >= 12000:
            if cat_s1:
                for i in cat_s1:
                    if i in cat_uptala:
                        j += 1
                        cat_s1.remove(i)
                        if j == 1:
                            break

                    else:
                            if order_s1:
                                for i in order_s1:
                                    if i >= 2000:
                                        j += 1
                                        order_s1.remove(i)
                                        if j == 1:
                                            break

                                if j == 1:
                                    for i in order_s1:
                                        if i >= 1000:
                                            j += 1
                                            order_s1.remove(i)
                                            if j == 2:
                                                break

                                    if j == 2:
                                        for i in order_s1:
                                            if i >= 50:
                                                j += 1

                                            else:
                                                flag = 1

                                        if j >= 3 and flag != 1:
                                            Category.objects.create(OwnerCategory='tala', stars=Stars('tala', Id), Id_id=Id)
                                            return HttpResponse('your group is tala')

                                        else:
                                            for i in order_s1:
                                                if i >= 1000:
                                                    j += 1
                                                    order_s1.remove(i)
                                                    if j == 1:
                                                        break

                                            if j == 1:
                                                for i in order_s1:
                                                    if i >= 500:
                                                        j += 1

                                            if j >= 2:
                                                Category.objects.create(OwnerCategory='noghre', stars=Stars('noghre', Id), Id_id=Id)
                                                return HttpResponse('your group is noghre')
                            else:
                                if order >= 200:
                                    Category.objects.create(OwnerCategory='platin', stars=Stars('platin', Id), Id_id=Id)
                                    return HttpResponse('your group is platin')

                                elif order >= 50:
                                    Category.objects.create(OwnerCategory='moshaver_mostaghel', stars=Stars('moshaver_mostaghel', Id), Id_id=Id)
                                    return HttpResponse('your group is moshaver_mostaghel')

                                else:
                                    return HttpResponse('you dont have category')



                if j == 1:
                    for i in order_s1:
                        if i >= 2000:
                            j += 1
                            order_s1.remove(i)
                            if j == 2:
                                break

                    if j == 2:
                        for i in order_s1:
                            if i >= 500:
                                j += 1

                            else:
                                flag = 1

                        if j >= 3 and flag != 1:
                            Category.objects.create(OwnerCategory='morvarid', stars=Stars('morvarid', Id), Id_id=Id)
                            return HttpResponse('your group is morvarid')

            else:
                if order >= 4000:
                    if order_s1:
                        for i in order_s1:
                            if i >= 2000:
                                j += 1
                                order_s1.remove(i)
                                if j == 1:
                                    break

                        if j == 1:
                            for i in order_s1:
                                if i >= 1000:
                                    j += 1
                                    order_s1.remove(i)
                                    if j == 2:
                                        break

                            if j == 2:
                                for i in order_s1:
                                    if i >= 50:
                                        j += 1

                                    else:
                                        flag = 1

                                if j >= 3 and flag != 1:
                                    Category.objects.create(OwnerCategory='tala', stars=Stars('tala', Id), Id_id=Id)
                                    return HttpResponse('your group is tala')

                        else:
                            for i in order_s1:
                                if i >= 1000:
                                    j += 1
                                    order_s1.remove(i)
                                    if j == 1:
                                        break

                            if j == 1:
                                for i in order_s1:
                                    if i >= 500:
                                        j += 1

                                if j >= 2:
                                    Category.objects.create(OwnerCategory='noghre', stars=Stars('noghre', Id), Id_id=Id)
                                    return HttpResponse('your group is noghre')

    if order >= 2000:
        if order_s1:
            for i in order_s1:
                if i >= 1000:
                    j += 1
                    if j == 1:
                        order_s1.remove(i)
                        break

            if j == 1:
                for i in order_s1:
                    if i >= 500:
                        j += 1
                        if j == 2:
                            order_s1.remove(i)
                            break

            if j >= 2:
                Category.objects.create(OwnerCategory='noghre', stars=Stars('noghre', Id), Id_id=Id)
                return HttpResponse('your group is noghre')

            else:
                if order >= 1000:
                    for i in order_s1:
                        if i >= 500:
                            j += 1
                            order_s1.remove(i)
                            if j == 1:
                                break

                    if j == 1:
                        for i in order_s1:
                            if i >= 200:
                                j += 1

                    if j >= 2:
                        Category.objects.create(OwnerCategory='bronze', stars=Stars('bronze', Id), Id_id=Id)
                        return HttpResponse('your group is bronze')

                    else:
                        if order >= 200:
                            Category.objects.create(OwnerCategory='platin', stars=Stars('platin', Id), Id_id=Id)
                            return HttpResponse('your group is platin')

                        elif order >= 50:
                            Category.objects.create(OwnerCategory='moshaver_mostaghel', stars=Stars('moshaver_mostaghel', Id), Id_id=Id)
                            return HttpResponse('your group is moshaver_mostaghel')
                        else:
                            return HttpResponse('you,re not in ranking list')
        else:
            if order >= 200:
                Category.objects.create(OwnerCategory='platin', stars=Stars('platin', Id), Id_id=Id)
                return HttpResponse('your group is platin')


            elif order >= 50:

                Category.objects.create(OwnerCategory='moshaver_mostaghel', stars=Stars('moshaver_mostaghel', Id), Id_id=Id)

                return HttpResponse('your group is moshaver_mostaghel')

            else:

                return HttpResponse('you,re not in ranking list')

    else:
        if order >= 1000:
            for i in order_s1:
                if i >= 500:
                    j += 1
                    order_s1.remove(i)
                    if j == 1:
                        break

            if j == 1:
                for i in order_s1:
                    if i >= 200:
                        j += 1

            if j >= 2:
                Category.objects.create(OwnerCategory='bronze', stars=Stars('bronze', Id), Id_id=Id)
                return HttpResponse('your group is bronze')

            else:
                if order >= 200:
                    Category.objects.create(OwnerCategory='platin', stars=Stars('platin', Id), Id_id=Id)
                    return HttpResponse('your group is platin')

                elif order >= 50:
                    Category.objects.create(OwnerCategory='moshaver_mostaghel', stars=Stars('moshaver_mostaghel', Id), Id_id=Id)
                    return HttpResponse('your group is moshaver_mostaghel')
                else:
                    return HttpResponse('you,re not in ranking list')

        else:
            if order >= 200:
                Category.objects.create(OwnerCategory='platin', stars=Stars('platin', Id), Id_id=Id)
                return HttpResponse('your group is platin')

            elif order >= 50:
                Category.objects.create(OwnerCategory='moshaver_mostaghel', stars=Stars('moshaver_mostaghel', Id), Id_id=Id)
                return HttpResponse('your group is moshaver_mostaghel')
            else:
                return HttpResponse('you,re not in ranking list')


def commision(request):

    # every order that append first must run this function

    category = Category.objects.filter(Id_id=request.user.id).first().OwnerCategory

    if category == 'moshaver_mostaghel':
        order = Order(request.user.id) * 10000
        order = float(order)
        list = order_list(request.user.id)
        list.append(order)
        sum_order = sum(list)

        commision = 1

        if sum_order > 2000000 and sum_order <= 10000000:
            commision = 0.01

        if sum_order > 10000000 and sum_order <= 20000000:
            commision = 0.02

        if sum_order > 20000000 and sum_order <= 30000000:
            commision = 0.03

        if sum_order > 30000000 and sum_order <= 40000000:
            commision = 0.04

        if sum_order > 40000000:
            commision = 0.05

        price = order - (order * commision)

        return HttpResponse(price)

    else:
        return HttpResponse('YOU DONT HAVE THIS COMMISION')


def compress(request):

    if request.user.is_authenticated:
        Id = request.user.id

    else:
        return HttpResponse('first login')

    # Id = 1

    if branches(Id) is not None:
        for br1 in branches(Id):
            if branches(br1.id):
                for br2 in branches(br1.id):
                    if branches(br2.id):
                        for br3 in branches(br2.id):
                            if branches(br3.id):
                                for br4 in branches(br3.id):
                                    if branches(br4.id):
                                        for br5 in branches(br4.id):
                                            if branches(br5.id):
                                                for br6 in branches(br5.id):
                                                    if branches(br6.id):
                                                        for br7 in branches(br6.id):
                                                            if branches(br7.id):
                                                                for br8 in branches(br7.id):
                                                                    if branches(br8.id):
                                                                        for br9 in branches(br8.id):
                                                                            if branches(br9.id):
                                                                                for br10 in branches(br9.id):
                                                                                    if branches(br10.id):
                                                                                        for br11 in branches(br10.id):
                                                                                            if branches(br11.id):
                                                                                                for br12 in branches(br11.id):
                                                                                                    if branches(br12.id):
                                                                                                        for br13 in branches(br12.id):
                                                                                                            if branches(br13.id):
                                                                                                                for br14 in branches(br13.id):
                                                                                                                    if branches(br14.id):
                                                                                                                        for br15 in branches(br14.id):
                                                                                                                            if orderb(br15.id) >= 1000000:
                                                                                                                                if orderb(br14.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br14.id)

                                                                                                                                elif orderb(br13.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br13.id)

                                                                                                                                elif orderb(br12.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br12.id)

                                                                                                                                elif orderb(br11.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br11.id)

                                                                                                                                elif orderb(br10.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br10.id)

                                                                                                                                elif orderb(br9.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br9.id)

                                                                                                                                elif orderb(br8.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br8.id)

                                                                                                                                elif orderb(br7.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br7.id)

                                                                                                                                elif orderb(br6.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br6.id)

                                                                                                                                elif orderb(br5.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br5.id)

                                                                                                                                elif orderb(br5.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br5.id)

                                                                                                                                elif orderb(br4.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br4.id)

                                                                                                                                elif orderb(br3.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br3.id)

                                                                                                                                elif orderb(br2.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br2.id)

                                                                                                                                elif orderb(br1.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=br1.id)

                                                                                                                                elif orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br15.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br14.id) >= 1000000:

                                                                                                                                    if orderb(br13.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id,CMlmOwner_id=br13.id)

                                                                                                                                    elif orderb(br12.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id,CMlmOwner_id=br12.id)

                                                                                                                                    elif orderb(br11.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id,CMlmOwner_id=br11.id)

                                                                                                                                    elif orderb(br10.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id,CMlmOwner_id=br10.id)

                                                                                                                                    elif orderb(br9.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id,CMlmOwner_id=br9.id)

                                                                                                                                    elif orderb(br8.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id,CMlmOwner_id=br8.id)

                                                                                                                                    elif orderb(br7.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id,CMlmOwner_id=br7.id)

                                                                                                                                    elif orderb(br6.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id,CMlmOwner_id=br6.id)

                                                                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id,CMlmOwner_id=br5.id)

                                                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br4.id)

                                                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id,CMlmOwner_id=br3.id)

                                                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id,CMlmOwner_id=br2.id)

                                                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id,CMlmOwner_id=br1.id)

                                                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br13.id) >= 1000000:

                                                                                                                                if orderb(br12.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br12.id)

                                                                                                                                elif orderb(br11.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br11.id)

                                                                                                                                elif orderb(br10.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br10.id)

                                                                                                                                elif orderb(br9.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br9.id)

                                                                                                                                elif orderb(br8.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br8.id)

                                                                                                                                elif orderb(br7.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br7.id)

                                                                                                                                elif orderb(br6.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br6.id)

                                                                                                                                elif orderb(br5.id) >= 1000000:
                                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br5.id)

                                                                                                                                elif orderb(br4.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br13.id, CMlmOwner_id=br4.id)

                                                                                                                                elif orderb(br3.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br3.id)

                                                                                                                                elif orderb(br2.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br2.id)

                                                                                                                                elif orderb(br1.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br1.id)

                                                                                                                                elif orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br13.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br12.id) >= 1000000:

                                                                                                                                if orderb(br11.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br11.id)

                                                                                                                                elif orderb(br10.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br10.id)

                                                                                                                                elif orderb(br9.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br9.id)

                                                                                                                                elif orderb(br8.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br8.id)

                                                                                                                                elif orderb(br7.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br7.id)

                                                                                                                                elif orderb(br6.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br6.id)

                                                                                                                                elif orderb(br5.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br5.id)

                                                                                                                                elif orderb(br4.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br12.id, CMlmOwner_id=br4.id)

                                                                                                                                elif orderb(br3.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br3.id)

                                                                                                                                elif orderb(br2.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br2.id)

                                                                                                                                elif orderb(br1.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br1.id)

                                                                                                                                elif orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br12.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br11.id) >= 1000000:

                                                                                                                                if orderb(br10.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br10.id)

                                                                                                                                elif orderb(br9.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br9.id)

                                                                                                                                elif orderb(br8.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br8.id)

                                                                                                                                elif orderb(br7.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br7.id)

                                                                                                                                elif orderb(br6.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br6.id)

                                                                                                                                elif orderb(br5.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br5.id)

                                                                                                                                elif orderb(br4.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br11.id, CMlmOwner_id=br4.id)

                                                                                                                                elif orderb(br3.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br3.id)

                                                                                                                                elif orderb(br2.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br2.id)

                                                                                                                                elif orderb(br1.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br1.id)

                                                                                                                                elif orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br11.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br10.id) >= 1000000:

                                                                                                                                if orderb(br9.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br9.id)

                                                                                                                                elif orderb(br8.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br8.id)

                                                                                                                                elif orderb(br7.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br7.id)

                                                                                                                                elif orderb(br6.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br6.id)

                                                                                                                                elif orderb(br5.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br5.id)

                                                                                                                                elif orderb(br4.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br10.id, CMlmOwner_id=br4.id)

                                                                                                                                elif orderb(br3.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br3.id)

                                                                                                                                elif orderb(br2.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br2.id)

                                                                                                                                elif orderb(br1.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br1.id)

                                                                                                                                elif orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br10.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br9.id) >= 1000000:

                                                                                                                                if orderb(br8.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br8.id)

                                                                                                                                elif orderb(br7.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br7.id)

                                                                                                                                elif orderb(br6.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br6.id)

                                                                                                                                elif orderb(br5.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br5.id)

                                                                                                                                elif orderb(br4.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br9.id, CMlmOwner_id=br4.id)

                                                                                                                                elif orderb(br3.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br3.id)

                                                                                                                                elif orderb(br2.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br2.id)

                                                                                                                                elif orderb(br1.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br1.id)

                                                                                                                                elif orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br9.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br8.id) >= 1000000:

                                                                                                                                if orderb(br7.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br7.id)

                                                                                                                                elif orderb(br6.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br6.id)

                                                                                                                                elif orderb(br5.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br5.id)

                                                                                                                                elif orderb(br4.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br8.id, CMlmOwner_id=br4.id)

                                                                                                                                elif orderb(br3.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br3.id)

                                                                                                                                elif orderb(br2.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br2.id)

                                                                                                                                elif orderb(br1.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br1.id)

                                                                                                                                elif orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br8.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br7.id) >= 1000000:

                                                                                                                                if orderb(br6.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br6.id)

                                                                                                                                elif orderb(br5.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br5.id)

                                                                                                                                elif orderb(br4.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br7.id, CMlmOwner_id=br4.id)

                                                                                                                                elif orderb(br3.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br3.id)

                                                                                                                                elif orderb(br2.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br2.id)

                                                                                                                                elif orderb(br1.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br1.id)

                                                                                                                                elif orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br7.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br6.id) >= 1000000:

                                                                                                                                if orderb(br5.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br5.id)

                                                                                                                                elif orderb(br4.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br6.id, CMlmOwner_id=br4.id)

                                                                                                                                elif orderb(br3.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br3.id)

                                                                                                                                elif orderb(br2.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br2.id)

                                                                                                                                elif orderb(br1.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br1.id)

                                                                                                                                elif orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br6.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br5.id) >= 1000000:

                                                                                                                                if orderb(br4.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br5.id, CMlmOwner_id=br4.id)

                                                                                                                                elif orderb(br3.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br3.id)

                                                                                                                                elif orderb(br2.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br2.id)

                                                                                                                                elif orderb(br1.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br1.id)

                                                                                                                                elif orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br5.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br4.id) >= 1000000:

                                                                                                                                if orderb(br3.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br3.id)

                                                                                                                                elif orderb(br2.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br2.id)

                                                                                                                                elif orderb(br1.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br1.id)

                                                                                                                                elif orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br4.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br3.id) >= 1000000:

                                                                                                                                if orderb(br2.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br2.id)

                                                                                                                                elif orderb(br1.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br1.id)

                                                                                                                                elif orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br3.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br2.id) >= 1000000:

                                                                                                                                if orderb(br1.id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=br1.id)

                                                                                                                                elif orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br2.id, CMlmOwner_id=Id)

                                                                                                                            elif orderb(br1.id) >= 1000000:

                                                                                                                                if orderb(Id) >= 1000000:
                                                                                                                                    Compress.objects.create(CMlmUser_id=br1.id, CMlmOwner_id=Id)




                                                                                                                    else:
                                                                                                                        if orderb(br14.id) >= 1000000:

                                                                                                                            if orderb(br13.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br13.id)

                                                                                                                            elif orderb(br12.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br12.id)

                                                                                                                            elif orderb(br11.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br11.id)

                                                                                                                            elif orderb(br10.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br10.id)

                                                                                                                            elif orderb(br9.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br9.id)

                                                                                                                            elif orderb(br8.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br8.id)

                                                                                                                            elif orderb(br7.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br7.id)

                                                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br6.id)

                                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br5.id)

                                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br4.id)

                                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br3.id)

                                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br2.id)

                                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=br1.id)

                                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br14.id, CMlmOwner_id=Id)

                                                                                                                        elif orderb(br13.id) >= 1000000:

                                                                                                                            if orderb(br12.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br12.id)

                                                                                                                            elif orderb(br11.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br11.id)

                                                                                                                            elif orderb(br10.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br10.id)

                                                                                                                            elif orderb(br9.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br9.id)

                                                                                                                            elif orderb(br8.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br8.id)

                                                                                                                            elif orderb(br7.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br7.id)

                                                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br6.id)

                                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br5.id)

                                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br4.id)

                                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br3.id)

                                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br2.id)

                                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br1.id)

                                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=Id)

                                                                                                                        elif orderb(br12.id) >= 1000000:

                                                                                                                            if orderb(br11.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br11.id)

                                                                                                                            elif orderb(br10.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br10.id)

                                                                                                                            elif orderb(br9.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br9.id)

                                                                                                                            elif orderb(br8.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br8.id)

                                                                                                                            elif orderb(br7.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br7.id)

                                                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br6.id)

                                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br5.id)

                                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br4.id)

                                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br3.id)

                                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br2.id)

                                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br1.id)

                                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=Id)

                                                                                                                        elif orderb(br11.id) >= 1000000:

                                                                                                                            if orderb(br10.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br10.id)

                                                                                                                            elif orderb(br9.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br9.id)

                                                                                                                            elif orderb(br8.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br8.id)

                                                                                                                            elif orderb(br7.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br7.id)

                                                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br6.id)

                                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br5.id)

                                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br4.id)

                                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br3.id)

                                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br2.id)

                                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br1.id)

                                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=Id)

                                                                                                                        elif orderb(br10.id) >= 1000000:

                                                                                                                            if orderb(br9.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br9.id)

                                                                                                                            elif orderb(br8.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br8.id)

                                                                                                                            elif orderb(br7.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br7.id)

                                                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br6.id)

                                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br5.id)

                                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br4.id)

                                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br3.id)

                                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br2.id)

                                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br1.id)

                                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=Id)

                                                                                                                        elif orderb(br9.id) >= 1000000:

                                                                                                                            if orderb(br8.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br8.id)

                                                                                                                            elif orderb(br7.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br7.id)

                                                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br6.id)

                                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br5.id)

                                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br4.id)

                                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br3.id)

                                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br2.id)

                                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br1.id)

                                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=Id)

                                                                                                                        elif orderb(br8.id) >= 1000000:

                                                                                                                            if orderb(br7.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br7.id)

                                                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br6.id)

                                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br5.id)

                                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br4.id)

                                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br3.id)

                                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br2.id)

                                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br1.id)

                                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=Id)

                                                                                                                        elif orderb(br7.id) >= 1000000:

                                                                                                                            if orderb(br6.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br6.id)

                                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br5.id)

                                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br4.id)

                                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br3.id)

                                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br2.id)

                                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br1.id)

                                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=Id)

                                                                                                                        elif orderb(br6.id) >= 1000000:

                                                                                                                            if orderb(br5.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br5.id)

                                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br4.id)

                                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br3.id)

                                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br2.id)

                                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br1.id)

                                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=Id)

                                                                                                                        elif orderb(br5.id) >= 1000000:

                                                                                                                            if orderb(br4.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br4.id)

                                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br3.id)

                                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br2.id)

                                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br1.id)

                                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=Id)

                                                                                                                        elif orderb(br4.id) >= 1000000:

                                                                                                                            if orderb(br3.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br3.id)

                                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br2.id)

                                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br1.id)

                                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=Id)

                                                                                                                        elif orderb(br3.id) >= 1000000:

                                                                                                                            if orderb(br2.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br2.id)

                                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br1.id)

                                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=Id)

                                                                                                                        elif orderb(br2.id) >= 1000000:

                                                                                                                            if orderb(br1.id) >= 1000000:
                                                                                                                                Compress.objects.create(
                                                                                                                                    CMlmUser_id=br2.id,
                                                                                                                                    CMlmOwner_id=br1.id)

                                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=Id)

                                                                                                                        elif orderb(br1.id) >= 1000000:

                                                                                                                            if orderb(Id) >= 1000000:
                                                                                                                                Compress.objects.create(CMlmUser_id=br1.id,CMlmOwner_id=Id)


                                                                                                            else:

                                                                                                                if orderb(br13.id) >= 1000000:

                                                                                                                    if orderb(br12.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br12.id)

                                                                                                                    elif orderb(br11.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br11.id)

                                                                                                                    elif orderb(br10.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br10.id)

                                                                                                                    elif orderb(br9.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br9.id)

                                                                                                                    elif orderb(br8.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br8.id)

                                                                                                                    elif orderb(br7.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br7.id)

                                                                                                                    elif orderb(br6.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br6.id)

                                                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br5.id)

                                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br4.id)

                                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br3.id)

                                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br2.id)

                                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=br1.id)

                                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br13.id,CMlmOwner_id=Id)

                                                                                                                elif orderb(br12.id) >= 1000000:

                                                                                                                    if orderb(br11.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br11.id)

                                                                                                                    elif orderb(br10.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br10.id)

                                                                                                                    elif orderb(br9.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br9.id)

                                                                                                                    elif orderb(br8.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br8.id)

                                                                                                                    elif orderb(br7.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br7.id)

                                                                                                                    elif orderb(br6.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br6.id)

                                                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br5.id)

                                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br4.id)

                                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br3.id)

                                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br2.id)

                                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br1.id)

                                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=Id)

                                                                                                                elif orderb(br11.id) >= 1000000:

                                                                                                                    if orderb(br10.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br10.id)

                                                                                                                    elif orderb(br9.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br9.id)

                                                                                                                    elif orderb(br8.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br8.id)

                                                                                                                    elif orderb(br7.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br7.id)

                                                                                                                    elif orderb(br6.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br6.id)

                                                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br5.id)

                                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br4.id)

                                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br3.id)

                                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br2.id)

                                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br1.id)

                                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=Id)

                                                                                                                elif orderb(br10.id) >= 1000000:

                                                                                                                    if orderb(br9.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br9.id)

                                                                                                                    elif orderb(br8.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br8.id)

                                                                                                                    elif orderb(br7.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br7.id)

                                                                                                                    elif orderb(br6.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br6.id)

                                                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br5.id)

                                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br4.id)

                                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br3.id)

                                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br2.id)

                                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br1.id)

                                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=Id)

                                                                                                                elif orderb(br9.id) >= 1000000:

                                                                                                                    if orderb(br8.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br8.id)

                                                                                                                    elif orderb(br7.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br7.id)

                                                                                                                    elif orderb(br6.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br6.id)

                                                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br5.id)

                                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br4.id)

                                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br3.id)

                                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br2.id)

                                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br1.id)

                                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=Id)

                                                                                                                elif orderb(br8.id) >= 1000000:

                                                                                                                    if orderb(br7.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br8.id, CMlmOwner_id=br7.id)

                                                                                                                    elif orderb(br6.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br6.id)

                                                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br5.id)

                                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br4.id)

                                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br3.id)

                                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br2.id)

                                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br1.id)

                                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=Id)

                                                                                                                elif orderb(br7.id) >= 1000000:

                                                                                                                    if orderb(br6.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br6.id)

                                                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br5.id)

                                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br4.id)

                                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br3.id)

                                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br2.id)

                                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br1.id)

                                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=Id)

                                                                                                                elif orderb(br6.id) >= 1000000:

                                                                                                                    if orderb(br5.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br5.id)

                                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br4.id)

                                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br3.id)

                                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br2.id)

                                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br1.id)

                                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=Id)

                                                                                                                elif orderb(br5.id) >= 1000000:

                                                                                                                    if orderb(br4.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br4.id)

                                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br3.id)

                                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br2.id)

                                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br1.id)

                                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=Id)

                                                                                                                elif orderb(br4.id) >= 1000000:

                                                                                                                    if orderb(br3.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br3.id)

                                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br2.id)

                                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br1.id)

                                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=Id)

                                                                                                                elif orderb(br3.id) >= 1000000:

                                                                                                                    if orderb(br2.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br2.id)

                                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br1.id)

                                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=Id)

                                                                                                                elif orderb(br2.id) >= 1000000:

                                                                                                                    if orderb(br1.id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=br1.id)

                                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=Id)

                                                                                                                elif orderb(br1.id) >= 1000000:

                                                                                                                    if orderb(Id) >= 1000000:
                                                                                                                        Compress.objects.create(CMlmUser_id=br1.id,CMlmOwner_id=Id)



                                                                                                    else:
                                                                                                        if orderb(br12.id) >= 1000000:

                                                                                                            if orderb(br11.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br11.id)

                                                                                                            elif orderb(br10.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br10.id)

                                                                                                            elif orderb(br9.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br9.id)

                                                                                                            elif orderb(br8.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br8.id)

                                                                                                            elif orderb(br7.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br7.id)

                                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br6.id)

                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br5.id)

                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br4.id)

                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br3.id)

                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br2.id)

                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=br1.id)

                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br12.id,CMlmOwner_id=Id)

                                                                                                        elif orderb(br11.id) >= 1000000:

                                                                                                            if orderb(br10.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br10.id)

                                                                                                            elif orderb(br9.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br9.id)

                                                                                                            elif orderb(br8.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br8.id)

                                                                                                            elif orderb(br7.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br7.id)

                                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br6.id)

                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br5.id)

                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br4.id)

                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br3.id)

                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br2.id)

                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br1.id)

                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=Id)

                                                                                                        elif orderb(br10.id) >= 1000000:

                                                                                                            if orderb(br9.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br9.id)

                                                                                                            elif orderb(br8.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br8.id)

                                                                                                            elif orderb(br7.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br7.id)

                                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br6.id)

                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br5.id)

                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br4.id)

                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br3.id)

                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br2.id)

                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br1.id)

                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=Id)

                                                                                                        elif orderb(br9.id) >= 1000000:

                                                                                                            if orderb(br8.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br8.id)

                                                                                                            elif orderb(br7.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br7.id)

                                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br6.id)

                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br5.id)

                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br4.id)

                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br3.id)

                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br2.id)

                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br1.id)

                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=Id)

                                                                                                        elif orderb(br8.id) >= 1000000:

                                                                                                            if orderb(br7.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br7.id)

                                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br6.id)

                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br5.id)

                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br4.id)

                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br3.id)

                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br2.id)

                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br1.id)

                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=Id)

                                                                                                        elif orderb(br7.id) >= 1000000:

                                                                                                            if orderb(br6.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br6.id)

                                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br5.id)

                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br4.id)

                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br3.id)

                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br2.id)

                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br1.id)

                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=Id)

                                                                                                        elif orderb(br6.id) >= 1000000:

                                                                                                            if orderb(br5.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br5.id)

                                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br4.id)

                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br3.id)

                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br2.id)

                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br1.id)

                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=Id)

                                                                                                        elif orderb(br5.id) >= 1000000:

                                                                                                            if orderb(br4.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br4.id)

                                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br3.id)

                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br2.id)

                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br1.id)

                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=Id)

                                                                                                        elif orderb(br4.id) >= 1000000:

                                                                                                            if orderb(br3.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br3.id)

                                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br2.id)

                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br1.id)

                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=Id)

                                                                                                        elif orderb(br3.id) >= 1000000:

                                                                                                            if orderb(br2.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br2.id)

                                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br1.id)

                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=Id)

                                                                                                        elif orderb(br2.id) >= 1000000:

                                                                                                            if orderb(br1.id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=br1.id)

                                                                                                            elif orderb(Id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=Id)

                                                                                                        elif orderb(br1.id) >= 1000000:

                                                                                                            if orderb(Id) >= 1000000:
                                                                                                                Compress.objects.create(CMlmUser_id=br1.id,CMlmOwner_id=Id)


                                                                                            else:
                                                                                                if orderb(br11.id) >= 1000000:

                                                                                                    if orderb(br10.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br10.id)

                                                                                                    elif orderb(br9.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br9.id)

                                                                                                    elif orderb(br8.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br8.id)

                                                                                                    elif orderb(br7.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br7.id)

                                                                                                    elif orderb(br6.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br6.id)

                                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br5.id)

                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br4.id)

                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br3.id)

                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br2.id)

                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=br1.id)

                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br11.id,CMlmOwner_id=Id)

                                                                                                elif orderb(br10.id) >= 1000000:

                                                                                                    if orderb(br9.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br9.id)

                                                                                                    elif orderb(br8.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br8.id)

                                                                                                    elif orderb(br7.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br7.id)

                                                                                                    elif orderb(br6.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br6.id)

                                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br5.id)

                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br4.id)

                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br3.id)

                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br2.id)

                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br1.id)

                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=Id)

                                                                                                elif orderb(br9.id) >= 1000000:

                                                                                                    if orderb(br8.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br8.id)

                                                                                                    elif orderb(br7.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br7.id)

                                                                                                    elif orderb(br6.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br6.id)

                                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br5.id)

                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br4.id)

                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br3.id)

                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br2.id)

                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br1.id)

                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=Id)

                                                                                                elif orderb(br8.id) >= 1000000:

                                                                                                    if orderb(br7.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br7.id)

                                                                                                    elif orderb(br6.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br6.id)

                                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br5.id)

                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br4.id)

                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br3.id)

                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br2.id)

                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br1.id)

                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=Id)

                                                                                                elif orderb(br7.id) >= 1000000:

                                                                                                    if orderb(br6.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br6.id)

                                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br5.id)

                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br4.id)

                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br3.id)

                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br2.id)

                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br1.id)

                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=Id)

                                                                                                elif orderb(br6.id) >= 1000000:

                                                                                                    if orderb(br5.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br5.id)

                                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br4.id)

                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br3.id)

                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br2.id)

                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br1.id)

                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=Id)

                                                                                                elif orderb(br5.id) >= 1000000:

                                                                                                    if orderb(br4.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br4.id)

                                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br3.id)

                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br2.id)

                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br1.id)

                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=Id)

                                                                                                elif orderb(br4.id) >= 1000000:

                                                                                                    if orderb(br3.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br3.id)

                                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br2.id)

                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br1.id)

                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=Id)

                                                                                                elif orderb(br3.id) >= 1000000:

                                                                                                    if orderb(br2.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br3.id, CMlmOwner_id=br2.id)

                                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br1.id)

                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=Id)

                                                                                                elif orderb(br2.id) >= 1000000:

                                                                                                    if orderb(br1.id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=br1.id)

                                                                                                    elif orderb(Id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=Id)

                                                                                                elif orderb(br1.id) >= 1000000:

                                                                                                    if orderb(Id) >= 1000000:
                                                                                                        Compress.objects.create(CMlmUser_id=br1.id,CMlmOwner_id=Id)


                                                                                    else:

                                                                                        if orderb(br10.id) >= 1000000:

                                                                                            if orderb(br9.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br9.id)

                                                                                            elif orderb(br8.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br8.id)

                                                                                            elif orderb(br7.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br7.id)

                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br6.id)

                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br5.id)

                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br4.id)

                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br3.id)

                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br2.id)

                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=br1.id)

                                                                                            elif orderb(Id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br10.id,CMlmOwner_id=Id)

                                                                                        elif orderb(br9.id) >= 1000000:

                                                                                            if orderb(br8.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br8.id)

                                                                                            elif orderb(br7.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br7.id)

                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br6.id)

                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br5.id)

                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br4.id)

                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br3.id)

                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br2.id)

                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br1.id)

                                                                                            elif orderb(Id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=Id)

                                                                                        elif orderb(br8.id) >= 1000000:

                                                                                            if orderb(br7.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br7.id)

                                                                                            elif orderb(br6.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br6.id)

                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br5.id)

                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br4.id)

                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br3.id)

                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br2.id)

                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br1.id)

                                                                                            elif orderb(Id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=Id)

                                                                                        elif orderb(br7.id) >= 1000000:

                                                                                            if orderb(br6.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br6.id)

                                                                                            elif orderb(br5.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br5.id)

                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br4.id)

                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br3.id)

                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br2.id)

                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br1.id)

                                                                                            elif orderb(Id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=Id)

                                                                                        elif orderb(br6.id) >= 1000000:

                                                                                            if orderb(br5.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br5.id)

                                                                                            elif orderb(br4.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br4.id)

                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br3.id)

                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br2.id)

                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br1.id)

                                                                                            elif orderb(Id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=Id)

                                                                                        elif orderb(br5.id) >= 1000000:

                                                                                            if orderb(br4.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br4.id)

                                                                                            elif orderb(br3.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br3.id)

                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br2.id)

                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br1.id)

                                                                                            elif orderb(Id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=Id)

                                                                                        elif orderb(br4.id) >= 1000000:

                                                                                            if orderb(br3.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br3.id)

                                                                                            elif orderb(br2.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br2.id)

                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br1.id)

                                                                                            elif orderb(Id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=Id)

                                                                                        elif orderb(br3.id) >= 1000000:

                                                                                            if orderb(br2.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br2.id)

                                                                                            elif orderb(br1.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br1.id)

                                                                                            elif orderb(Id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=Id)

                                                                                        elif orderb(br2.id) >= 1000000:

                                                                                            if orderb(br1.id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=br1.id)

                                                                                            elif orderb(Id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=Id)

                                                                                        elif orderb(br1.id) >= 1000000:

                                                                                            if orderb(Id) >= 1000000:
                                                                                                Compress.objects.create(CMlmUser_id=br1.id,CMlmOwner_id=Id)

                                                                            else:
                                                                                if orderb(br9.id) >= 1000000:

                                                                                    if orderb(br8.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br8.id)

                                                                                    elif orderb(br7.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br7.id)

                                                                                    elif orderb(br6.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br6.id)

                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br5.id)

                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br4.id)

                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br3.id)

                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br2.id)

                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=br1.id)

                                                                                    elif orderb(Id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br9.id,CMlmOwner_id=Id)

                                                                                elif orderb(br8.id) >= 1000000:

                                                                                    if orderb(br7.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br7.id)

                                                                                    elif orderb(br6.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br6.id)

                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br5.id)

                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br4.id)

                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br3.id)

                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br2.id)

                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br1.id)

                                                                                    elif orderb(Id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=Id)

                                                                                elif orderb(br7.id) >= 1000000:

                                                                                    if orderb(br6.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br6.id)

                                                                                    elif orderb(br5.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br5.id)

                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br4.id)

                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br3.id)

                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br2.id)

                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br1.id)

                                                                                    elif orderb(Id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=Id)

                                                                                elif orderb(br6.id) >= 1000000:

                                                                                    if orderb(br5.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br5.id)

                                                                                    elif orderb(br4.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br4.id)

                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br3.id)

                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br2.id)

                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br1.id)

                                                                                    elif orderb(Id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=Id)

                                                                                elif orderb(br5.id) >= 1000000:

                                                                                    if orderb(br4.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br4.id)

                                                                                    elif orderb(br3.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br3.id)

                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br2.id)

                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br1.id)

                                                                                    elif orderb(Id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=Id)

                                                                                elif orderb(br4.id) >= 1000000:

                                                                                    if orderb(br3.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br3.id)

                                                                                    elif orderb(br2.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br2.id)

                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br1.id)

                                                                                    elif orderb(Id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=Id)

                                                                                elif orderb(br3.id) >= 1000000:

                                                                                    if orderb(br2.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br2.id)

                                                                                    elif orderb(br1.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br1.id)

                                                                                    elif orderb(Id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=Id)

                                                                                elif orderb(br2.id) >= 1000000:

                                                                                    if orderb(br1.id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=br1.id)

                                                                                    elif orderb(Id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=Id)

                                                                                elif orderb(br1.id) >= 1000000:

                                                                                    if orderb(Id) >= 1000000:
                                                                                        Compress.objects.create(CMlmUser_id=br1.id,CMlmOwner_id=Id)


                                                                    else:
                                                                        if orderb(br8.id) >= 1000000:

                                                                            if orderb(br7.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br7.id)

                                                                            elif orderb(br6.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br6.id)

                                                                            elif orderb(br5.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br5.id)

                                                                            elif orderb(br4.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br4.id)

                                                                            elif orderb(br3.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br3.id)

                                                                            elif orderb(br2.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br2.id)

                                                                            elif orderb(br1.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br8.id,CMlmOwner_id=br1.id)

                                                                            elif orderb(Id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br8.id, CMlmOwner_id=Id)

                                                                        elif orderb(br7.id) >= 1000000:

                                                                            if orderb(br6.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br6.id)

                                                                            elif orderb(br5.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br5.id)

                                                                            elif orderb(br4.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br4.id)

                                                                            elif orderb(br3.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br3.id)

                                                                            elif orderb(br2.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br2.id)

                                                                            elif orderb(br1.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br1.id)

                                                                            elif orderb(Id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br7.id, CMlmOwner_id=Id)

                                                                        elif orderb(br6.id) >= 1000000:

                                                                            if orderb(br5.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br5.id)

                                                                            elif orderb(br4.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br4.id)

                                                                            elif orderb(br3.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br3.id)

                                                                            elif orderb(br2.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br2.id)

                                                                            elif orderb(br1.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br1.id)

                                                                            elif orderb(Id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br6.id, CMlmOwner_id=Id)

                                                                        elif orderb(br5.id) >= 1000000:

                                                                            if orderb(br4.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br4.id)

                                                                            elif orderb(br3.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br3.id)

                                                                            elif orderb(br2.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br2.id)

                                                                            elif orderb(br1.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br1.id)

                                                                            elif orderb(Id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br5.id, CMlmOwner_id=Id)

                                                                        elif orderb(br4.id) >= 1000000:

                                                                            if orderb(br3.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br3.id)

                                                                            elif orderb(br2.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br2.id)

                                                                            elif orderb(br1.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br1.id)

                                                                            elif orderb(Id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br4.id, CMlmOwner_id=Id)

                                                                        elif orderb(br3.id) >= 1000000:

                                                                            if orderb(br2.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br2.id)

                                                                            elif orderb(br1.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br1.id)

                                                                            elif orderb(Id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br3.id, CMlmOwner_id=Id)

                                                                        elif orderb(br2.id) >= 1000000:

                                                                            if orderb(br1.id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=br1.id)

                                                                            elif orderb(Id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br2.id, CMlmOwner_id=Id)

                                                                        elif orderb(br1.id) >= 1000000:

                                                                            if orderb(Id) >= 1000000:
                                                                                Compress.objects.create(CMlmUser_id=br1.id, CMlmOwner_id=Id)

                                                            else:
                                                                if orderb(br7.id) >= 1000000:

                                                                    if orderb(br6.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br6.id)

                                                                    elif orderb(br5.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br5.id)

                                                                    elif orderb(br4.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br4.id)

                                                                    elif orderb(br3.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br3.id)

                                                                    elif orderb(br2.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br2.id)

                                                                    elif orderb(br1.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=br1.id)

                                                                    elif orderb(Id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br7.id,CMlmOwner_id=Id)

                                                                elif orderb(br6.id) >= 1000000:

                                                                    if orderb(br5.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br5.id)

                                                                    elif orderb(br4.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br4.id)

                                                                    elif orderb(br3.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br3.id)

                                                                    elif orderb(br2.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br2.id)

                                                                    elif orderb(br1.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br1.id)

                                                                    elif orderb(Id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=Id)

                                                                elif orderb(br5.id) >= 1000000:

                                                                    if orderb(br4.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br4.id)

                                                                    elif orderb(br3.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br3.id)

                                                                    elif orderb(br2.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br2.id)

                                                                    elif orderb(br1.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br1.id)

                                                                    elif orderb(Id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=Id)

                                                                elif orderb(br4.id) >= 1000000:

                                                                    if orderb(br3.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br3.id)

                                                                    elif orderb(br2.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br2.id)

                                                                    elif orderb(br1.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br1.id)

                                                                    elif orderb(Id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=Id)

                                                                elif orderb(br3.id) >= 1000000:

                                                                    if orderb(br2.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br2.id)

                                                                    elif orderb(br1.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br1.id)

                                                                    elif orderb(Id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=Id)

                                                                elif orderb(br2.id) >= 1000000:

                                                                    if orderb(br1.id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=br1.id)

                                                                    elif orderb(Id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=Id)

                                                                elif orderb(br1.id) >= 1000000:

                                                                    if orderb(Id) >= 1000000:
                                                                        Compress.objects.create(CMlmUser_id=br1.id,CMlmOwner_id=Id)


                                                    else:
                                                        if orderb(br6.id) >= 1000000:

                                                            if orderb(br5.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br5.id)

                                                            elif orderb(br4.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br4.id)

                                                            elif orderb(br3.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br3.id)

                                                            elif orderb(br2.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br2.id)

                                                            elif orderb(br1.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=br1.id)

                                                            elif orderb(Id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br6.id,CMlmOwner_id=Id)

                                                        elif orderb(br5.id) >= 1000000:

                                                            if orderb(br4.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br4.id)

                                                            elif orderb(br3.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br3.id)

                                                            elif orderb(br2.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br2.id)

                                                            elif orderb(br1.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=br1.id)

                                                            elif orderb(Id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br5.id,CMlmOwner_id=Id)

                                                        elif orderb(br4.id) >= 1000000:

                                                            if orderb(br3.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br3.id)

                                                            elif orderb(br2.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br2.id)

                                                            elif orderb(br1.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=br1.id)

                                                            elif orderb(Id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br4.id,CMlmOwner_id=Id)

                                                        elif orderb(br3.id) >= 1000000:

                                                            if orderb(br2.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br2.id)

                                                            elif orderb(br1.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=br1.id)

                                                            elif orderb(Id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br3.id,CMlmOwner_id=Id)

                                                        elif orderb(br2.id) >= 1000000:

                                                            if orderb(br1.id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=br1.id)

                                                            elif orderb(Id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br2.id,CMlmOwner_id=Id)

                                                        elif orderb(br1.id) >= 1000000:

                                                            if orderb(Id) >= 1000000:
                                                                Compress.objects.create(CMlmUser_id=br1.id,CMlmOwner_id=Id)

                                            else:
                                                if orderb(br5.id) >= 1000000:

                                                    if orderb(br4.id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br5.id, CMlmOwner_id=br4.id)

                                                    elif orderb(br3.id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br5.id, CMlmOwner_id=br3.id)

                                                    elif orderb(br2.id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br5.id, CMlmOwner_id=br2.id)

                                                    elif orderb(br1.id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br5.id, CMlmOwner_id=br1.id)

                                                    elif orderb(Id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br5.id, CMlmOwner_id=Id)

                                                elif orderb(br4.id) >= 1000000:

                                                    if orderb(br3.id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br4.id, CMlmOwner_id=br3.id)

                                                    elif orderb(br2.id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br4.id, CMlmOwner_id=br2.id)

                                                    elif orderb(br1.id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br4.id, CMlmOwner_id=br1.id)

                                                    elif orderb(Id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br4.id, CMlmOwner_id=Id)

                                                elif orderb(br3.id) >= 1000000:

                                                    if orderb(br2.id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br3.id, CMlmOwner_id=br2.id)

                                                    elif orderb(br1.id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br3.id, CMlmOwner_id=br1.id)

                                                    elif orderb(Id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br3.id, CMlmOwner_id=Id)

                                                elif orderb(br2.id) >= 1000000:

                                                    if orderb(br1.id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br2.id, CMlmOwner_id=br1.id)

                                                    elif orderb(Id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br2.id, CMlmOwner_id=Id)

                                                elif orderb(br1.id) >= 1000000:

                                                    if orderb(Id) >= 1000000:
                                                        Compress.objects.create(CMlmUser_id=br1.id, CMlmOwner_id=Id)


                                    else:
                                        if orderb(br4.id) >= 1000000:

                                            if orderb(br3.id) >= 1000000:
                                                Compress.objects.create(CMlmUser_id=br4.id, CMlmOwner_id=br3.id)

                                            elif orderb(br2.id) >= 1000000:
                                                Compress.objects.create(CMlmUser_id=br4.id, CMlmOwner_id=br2.id)

                                            elif orderb(br1.id) >= 1000000:
                                                Compress.objects.create(CMlmUser_id=br4.id, CMlmOwner_id=br1.id)

                                            elif orderb(Id) >= 1000000:
                                                Compress.objects.create(CMlmUser_id=br4.id, CMlmOwner_id=Id)

                                        elif orderb(br3.id) >= 1000000:

                                            if orderb(br2.id) >= 1000000:
                                                Compress.objects.create(CMlmUser_id=br3.id, CMlmOwner_id=br2.id)

                                            elif orderb(br1.id) >= 1000000:
                                                Compress.objects.create(CMlmUser_id=br3.id, CMlmOwner_id=br1.id)

                                            elif orderb(Id) >= 1000000:
                                                Compress.objects.create(CMlmUser_id=br3.id, CMlmOwner_id=Id)

                                        elif orderb(br2.id) >= 1000000:

                                            if orderb(br1.id) >= 1000000:
                                                Compress.objects.create(CMlmUser_id=br2.id, CMlmOwner_id=br1.id)

                                            elif orderb(Id) >= 1000000:
                                                Compress.objects.create(CMlmUser_id=br2.id, CMlmOwner_id=Id)

                                        elif orderb(br1.id) >= 1000000:

                                            if orderb(Id) >= 1000000:
                                                Compress.objects.create(CMlmUser_id=br1.id, CMlmOwner_id=Id)

                            else:
                                if orderb(br3.id) >= 1000000:

                                    if orderb(br2.id) >= 1000000:
                                        Compress.objects.create(CMlmUser_id=br3.id, CMlmOwner_id=br2.id)

                                    elif orderb(br1.id) >= 1000000:
                                        Compress.objects.create(CMlmUser_id=br3.id, CMlmOwner_id=br1.id)

                                    elif orderb(Id) >= 1000000:
                                        Compress.objects.create(CMlmUser_id=br3.id, CMlmOwner_id=Id)

                                elif orderb(br2.id) >= 1000000:

                                    if orderb(br1.id) >= 1000000:
                                        Compress.objects.create(CMlmUser_id=br2.id, CMlmOwner_id=br1.id)

                                    elif orderb(Id) >= 1000000:
                                        Compress.objects.create(CMlmUser_id=br2.id, CMlmOwner_id=Id)

                                elif orderb(br1.id) >= 1000000:

                                    if orderb(Id) >= 1000000:
                                        Compress.objects.create(CMlmUser_id=br1.id, CMlmOwner_id=Id)

                    else:
                        if orderb(br2.id) >= 1000000:

                            if orderb(br1.id) >= 1000000:
                                Compress.objects.create(CMlmUser_id=br2.id, CMlmOwner_id=br1.id)

                            elif orderb(Id) >= 1000000:
                                Compress.objects.create(CMlmUser_id=br2.id, CMlmOwner_id=Id)

                        elif orderb(br1.id) >= 1000000:

                            if orderb(Id) >= 1000000:
                                Compress.objects.create(CMlmUser_id=br1.id, CMlmOwner_id=Id)

            else:
                if orderb(br1.id) >= 1000000:

                    if orderb(Id) >= 1000000:
                        Compress.objects.create(CMlmUser_id=br1.id, CMlmOwner_id=Id)

    else:
        if Order(Id) >= 1000000:
            Compress.objects.create(CMlmUser_id=Id, CMlmOwner_id=Id)

        else:
            pass


    if Compress.objects.all() is not None:
        OWNER = None
        ownerId = 0
        for owner in Compress.objects.all():
            user = UserOwner.objects.filter(MlmUser_id=owner.CMlmOwner_id).first()
            if user is not None:
                ownerId = user.MlmOwner_id
                OWNER = user.MlmOwner

            while OWNER is not None:
                if orderb(ownerId) >= 1000000:
                    Compress.objects.create(CMlmUser_id=owner.CMlmOwner_id, CMlmOwner_id=ownerId)
                    break

                else:
                    owner2 = UserOwner.objects.filter(MlmUser_id=ownerId).first()
                    if owner2 is not None:
                        ownerId = owner2.MlmOwner_id
                        OWNER = owner2.MlmOwner

    else:
        pass

    return HttpResponse('COMPRESS...')


def surfacePursant(request):

    category = Category.objects.filter(Id_id=request.user.id).first().OwnerCategory
    # category = 'tala'
    categoryList = ['moshaver_mostaghel', 'platin', 'bronze', 'noghre', 'tala', 'morvarid']
    if request.user.is_authenticated:
        Id = request.user.id

    else:
        return HttpResponse('first login')
    s1 = []
    s2 = []
    s3 = []
    if branches(Id) is not None:
        for i in branches(Id):
            branchId1 = i.id
            order = orderb(i.id)
            s1.append(order)
            ownerId = Compress.objects.filter(CMlmOwner_id=branchId1).first()
            if ownerId is not None:
                if branches(branchId1) is not None:
                    for j in branches(branchId1):
                        branchId2 = j.national_code
                        ncId = UserOwner.objects.filter(MlmOwner__national_code=branchId2).first().id
                        order = orderb(ncId)
                        s2.append(order)
                        ownerId = Compress.objects.filter(CMlmOwner__id=branchId2).first()
                        if ownerId is not None:
                            if branches(branchId2) is not None:
                                for k in branches(branchId2):
                                    branchId3 = k.national_code
                                    ncId = UserOwner.objects.filter(MlmOwner__national_code=branchId3).first().id
                                    order = orderb(ncId)
                                    s3.append(order)
    print(s1)
    print(s2)
    print(s3)
    # s1 = [200, 300, 400, 500]
    # s2 = [100, 200, 500]
    # s3 = [200,400, 500]
    sumPursant = 0
    if category in categoryList:
        if s1:
            pursant1 = sum(s1)*0.03
            sumPursant += pursant1

        if s2:
            pursant2 = sum(s2)*0.02
            sumPursant += pursant2
        if s3:
            pursant3 = sum(s3)*0.01
            sumPursant += pursant3

    return HttpResponse(sumPursant)


def sellingPursant(request):

    category = Category.objects.filter(Id_id=request.user.id).order_by('-id').first().OwnerCategory
    # category = 'zomorod'
    s1 = 1
    s2 = 0.75
    s3 = 0.5
    sumco_t = 0
    stars = Category.objects.filter(Id_id=request.user.id).order_by('-id').first().stars
    # stars = 3

    order_s1 = []
    order_s2 = []
    order_s3 = []

    if request.user.is_authenticated:
        Id = request.user.id

    else:
        return HttpResponse('first login')

    if category == 'moshaver_mostaghel':
        return HttpResponse('YOU DONT HAVE THIS PURSANT')

    if category in ['tala', 'noghre', 'bronze', 'platin']:
       s = 1

    elif category in ['morvarid', 'yaghoot']:
        s = 2

    else:
        s = 3



    points = [120, 600, 1200, 2500, 7000, 20000, 55000, 200000, 720000, 2400000, 7200000, 20000000, 30000000, 30000001]
    differs = [120, 480, 600, 1300, 4500, 13000, 35000, 145000, 520000, 1680000, 4800000, 12800000, 10000000, 1]
    coefficients = [3.7, 3.4, 3.1, 2.8, 2.5, 2.2, 1.9, 1.6, 1.3, 1, 0.7, 0.4, 0.2, 0.05]
    if branches(Id) is not None:
        for i in branches(Id):
            branchId1 = i.id
            order = orderb(i.id)
            order_s1 = [order]
            ownerId = UserOwner.objects.filter(MlmOwner__id=branchId1).first()

            if ownerId is not None:
                if branches(branchId1) is not None:
                    for j in branches(branchId1):
                        branchId2 = j.id
                        order = orderb(j.id)
                        order_s2.append(order)
                        ownerId = UserOwner.objects.filter(MlmOwner__id=branchId2).first()
                        if ownerId is not None:
                            if branches(branchId2) is not None:
                                for k in branches(branchId2):
                                    order = orderb(k.id)
                                    order_s3.append(order)

            total_s1 = 0
            total_s2 = 0
            total_s3 = 0

            if s == 1:
                total_s1 = sum(order_s1) * s1

            if s == 2:
                total_s1 = sum(order_s1) * s1

                if order_s2:
                    total_s2 = sum(order_s2) * s2

            if s == 3:
                total_s1 = sum(order_s1) * s1

                if order_s2:
                        total_s2 = sum(order_s2) * s2

                if order_s3:
                        total_s3 = sum(order_s3) * s3

            point = total_s1 + total_s2 + total_s3

            sumco = 0

            for j in range(len(points)):
                point_f = points[j]
                co_f = coefficients[j]
                differ_f = differs[j]

                if point < point_f:

                    if point_f == 120:
                        point_s = 0

                    else:
                        point_s = points[j-1]

                    sumco += (point - point_s) * co_f
                    break

                else:
                    if point_f == 30000001:
                        differ_f = point - 30000000

                    sumco += differ_f * co_f
            sumco_t += sumco

    if stars == 3:
        star_pur = 0.034

    elif stars == 4:
        star_pur = 0.036

    elif stars == 5:
        star_pur = 0.038

    elif stars >= 6:
        star_pur = 0.04

    else:
        star_pur = 0


    final_pursant = sumco_t * star_pur * 10000
    print(stars)

    return HttpResponse(round(final_pursant, 2))


def premium(request):

    # first must run sellingPursant and return it in this function

    category = Category.objects.filter(Id_id=request.user.id).first().OwnerCategory

    stars = Category.objects.filter(Id_id=request.user.id).first().stars

    sellingPursant = request.GET.get('sellingPursant')

    if request.user.is_authenticated:
        Id = request.user.id

    else:
        return HttpResponse('LOGIN FIRST')

    prem_t = 0
    category_s1 = []
    category_s2 = []
    category_s3 = []
    category_s4 = []

    cat_upsafir_tala = ['safir_tala', 'safir_morvarid', 'safir_yaghoot', 'safir_zomorod', 'safir_almas', 'safir_almas_abi', 'safir_almas_sorkh']

    if branches(Id) is not None:
        for i in branches(Id):
                branchId1 = i.id
                categ = Category.objects.filter(Id_id=i.id).first()
                if categ is not None:
                    categ = Category.objects.filter(Id_id=i.id).first().OwnerCategory
                category_s1.append(categ)
                ownerId = UserOwner.objects.filter(MlmOwner__id=branchId1).first()
                if ownerId is not None:
                    if branches(branchId1) is not None:
                        for j in branches(branchId1):
                            branchId2 = j.id
                            categ = Category.objects.filter(Id_id=j.id).first()
                            if categ is not None:
                                categ = Category.objects.filter(Id_id=i.id).first().OwnerCategory
                            category_s2.append(categ)
                            ownerId = UserOwner.objects.filter(MlmOwner__id=branchId2).first()
                            if ownerId is not None:
                                if branches(branchId2) is not None:
                                    for k in branches(branchId2):
                                        branchId3 = k.id
                                        categ = Category.objects.filter(Id_id=k.id).first()
                                        if categ is not None:
                                            categ = Category.objects.filter(Id_id=i.id).first().OwnerCategory
                                        category_s3.append(categ)
                                        ownerId = UserOwner.objects.filter(MlmOwner__id=branchId3).first()
                                        if ownerId is not None:
                                            if branches(branchId3) is not None:
                                                for m in branches(branchId3):
                                                    categ = Category.objects.filter(Id_id=m.id).first()
                                                    if categ is not None:
                                                        categ = Category.objects.filter(Id_id=i.id).first().OwnerCategory

                                                    category_s4.append(categ)


    if category in ['moshaver_mostaghel', 'platin', 'noghre', 'bronze', 'tala', 'morvarid']:
        return HttpResponse('this is not for your category...')

    if category == 'yaghoot':
        for i in category_s1:
            if i == 'yaghoot':
                if stars == 6:
                    premium_pur = 0.06

                elif stars == 5:
                    premium_pur = 0.59

                elif stars == 4:
                    premium_pur = 0.58

                elif stars == 3:
                    premium_pur = 0.57

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

    if category == 'zomorod':
        for i in category_s1:
            if i == 'yaghoot' or i == 'zomorod':
                if stars == 6:
                    premium_pur = 0.07

                elif stars == 5:
                    premium_pur = 0.69

                elif stars == 4:
                    premium_pur = 0.68

                elif stars == 3:
                    premium_pur = 0.67

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

        for j in category_s2:
            if j == 'yaghoot' or j == 'zomorod':
                if stars == 6:
                    premium_pur = 0.06

                elif stars == 5:
                    premium_pur = 0.59

                elif stars == 4:
                    premium_pur = 0.58

                elif stars == 3:
                    premium_pur = 0.57

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

    if category == 'almas':
        for i in category_s1:
            if i == 'almas' or i == 'zomorod':
                if stars == 6:
                    premium_pur = 0.08

                elif stars == 5:
                    premium_pur = 0.79

                elif stars == 4:
                    premium_pur = 0.78

                elif stars == 3:
                    premium_pur = 0.77

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

        for j in category_s2:
            if j == 'almas' or j == 'zomorod':
                if stars == 6:
                    premium_pur = 0.07

                elif stars == 5:
                    premium_pur = 0.69

                elif stars == 4:
                    premium_pur = 0.68

                elif stars == 3:
                    premium_pur = 0.67

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

    if category == 'almas_abi':
        for i in category_s1:
            if i == 'almas' or i == 'almas_abi':
                if stars == 6:
                    premium_pur = 0.09

                elif stars == 5:
                    premium_pur = 0.89

                elif stars == 4:
                    premium_pur = 0.88

                elif stars == 3:
                    premium_pur = 0.87

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

        for j in category_s2:
            if j == 'almas' or j == 'almas_abi':
                if stars == 6:
                    premium_pur = 0.08

                elif stars == 5:
                    premium_pur = 0.79

                elif stars == 4:
                    premium_pur = 0.78

                elif stars == 3:
                    premium_pur = 0.77

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

        for k in category_s3:
            if k == 'almas' or k == 'almas_abi':
                if stars == 6:
                    premium_pur = 0.07

                elif stars == 5:
                    premium_pur = 0.69

                elif stars == 4:
                    premium_pur = 0.68

                elif stars == 3:
                    premium_pur = 0.67

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

    if category == 'almas_sorkh':
        for i in category_s1:
            if i == 'almas_sorkh' or i == 'almas_abi':
                if stars == 6:
                    premium_pur = 0.1

                elif stars == 5:
                    premium_pur = 0.99

                elif stars == 4:
                    premium_pur = 0.98

                elif stars == 3:
                    premium_pur = 0.97

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

        for j in category_s2:
            if j == 'almas_sorkh' or j == 'almas_abi':
                if stars == 6:
                    premium_pur = 0.09

                elif stars == 5:
                    premium_pur = 0.89

                elif stars == 4:
                    premium_pur = 0.88

                elif stars == 3:
                    premium_pur = 0.87

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

        for k in category_s3:
            if k == 'almas_sorkh' or k == 'almas_abi':
                if stars == 6:
                    premium_pur = 0.08

                elif stars == 5:
                    premium_pur = 0.79

                elif stars == 4:
                    premium_pur = 0.78

                elif stars == 3:
                    premium_pur = 0.77

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

    if category == 'almas_siah':
        for i in category_s1:
            if i == 'almas_sorkh' or i == 'almas_siah' or i == 'almas_abi':
                if stars == 6:
                    premium_pur = 0.11

                elif stars == 5:
                    premium_pur = 0.109

                elif stars == 4:
                    premium_pur = 0.108

                elif stars == 3:
                    premium_pur = 0.107

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

        for j in category_s2:
            if j == 'almas_sorkh' or j == 'almas_abi' or j == 'almas_siah':
                if stars == 6:
                    premium_pur = 0.1

                elif stars == 5:
                    premium_pur = 0.99

                elif stars == 4:
                    premium_pur = 0.98

                elif stars == 3:
                    premium_pur = 0.97

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

        for k in category_s3:
            if k == 'almas_sorkh' or k == 'almas_abi' or k == 'almas_siah':
                if stars == 6:
                    premium_pur = 0.09

                elif stars == 5:
                    premium_pur = 0.89

                elif stars == 4:
                    premium_pur = 0.88

                elif stars == 3:
                    premium_pur = 0.87

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

        for m in category_s4:
            if m == 'almas_sorkh' or m == 'almas_abi' or m == 'almas_siah':
                if stars == 6:
                    premium_pur = 0.08

                elif stars == 5:
                    premium_pur = 0.79

                elif stars == 4:
                    premium_pur = 0.78

                elif stars == 3:
                    premium_pur = 0.77

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

    if category in cat_upsafir_tala:
        for i in category_s1:
            if i == 'almas_sorkh' or i == 'almas_siah' or i in cat_upsafir_tala:
                if stars == 6:
                    premium_pur = 0.12

                elif stars == 5:
                    premium_pur = 0.119

                elif stars == 4:
                    premium_pur = 0.118

                elif stars == 3:
                    premium_pur = 0.117

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

        for j in category_s2:
            if j == 'almas_sorkh' or j == 'almas_siah' or j in cat_upsafir_tala:
                if stars == 6:
                    premium_pur = 0.11

                elif stars == 5:
                    premium_pur = 0.109

                elif stars == 4:
                    premium_pur = 0.108

                elif stars == 3:
                    premium_pur = 0.107

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

        for k in category_s3:
            if k == 'almas_sorkh' or k == 'almas_siah' or k in cat_upsafir_tala:
                if stars == 6:
                    premium_pur = 0.10

                elif stars == 5:
                    premium_pur = 0.99

                elif stars == 4:
                    premium_pur = 0.98

                elif stars == 3:
                    premium_pur = 0.97

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

        for m in category_s4:
            if m == 'almas_sorkh' or m == 'almas_siah' or m in cat_upsafir_tala:
                if stars == 6:
                    premium_pur = 0.09

                elif stars == 5:
                    premium_pur = 0.89

                elif stars == 4:
                    premium_pur = 0.88

                elif stars == 3:
                    premium_pur = 0.87

                else:
                    premium_pur = 0

                prem_t += sellingPursant * premium_pur

    return HttpResponse(round(prem_t, 2))














































